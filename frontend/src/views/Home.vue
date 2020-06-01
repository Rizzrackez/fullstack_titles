<template>
  <div>
   <button :disabled="!prevPage" @click="fetchTitles(prevPage)">&lt;</button>
   <button :disabled="!nextPage" @click="fetchTitles(nextPage)">&gt;</button>
   <table>
   <thead>
    <tr>
     <th>Name</th>
     <th>Year</th>
     <th>Descriptions</th>
     <th>Episode</th>
     <th>Remove</th>
    </tr>
   </thead>
   <tbody>
    <tr v-for="title in titles" :key="title.id">
     <td>{{ title.name }}</td>
     <td>{{ title.year }}</td>
     <td>{{ title.descriptions }}</td>
     <td>{{ title.episode }}</td>
     <td><button v-on:click="deleteTitle(title)">delete</button></td>
    </tr>
   </tbody>
  </table>

  <input placeholder="name" v-model="currentTitle.name">
  <input placeholder="year" v-model="currentTitle.year">
  <input placeholder="descriptions" v-model="currentTitle.descriptions">
  <input placeholder="episode" v-model="currentTitle.episode">
  <button v-on:click="createTitle()">Submit</button>

  </div>
</template>

<script>
const host = process.env.VUE_APP_BACKEND_HOST || 'http://127.0.0.1:8000';

export default {
  name: 'Home',

  data() {
    return {
      titles: [],
      currentTitle: {},
      nextPage: null,
      prevPage: null,
    };
  },
  async created() {
    this.fetchTitles();
  },
  methods: {
    async fetchTitles(url = `${host}/api/titles/`) {
      const response = await fetch(url);
      const { results, next, previous } = await response.json();
      this.titles = results;
      this.nextPage = next;
      this.prevPage = previous;
    },

    async createTitle() {
      const response = await fetch(`${host}/api/titles/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.currentTitle),
      });
      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchTitles();
    },

    async deleteTitle(title) {
      const { id } = title;
      const response = await fetch(`{$host}/api/titles/${id}/`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      if (response.status !== 204) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchTitles();
    },

  },
};
</script>
