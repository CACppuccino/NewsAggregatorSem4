<template>
  <div id="app">
    <h1>News Aggregator</h1>
    <input placeholder="Start your search" v-model="query"/>
    <button @click="search">search</button>
    <div v-for="item in res" :key="item._id" style="box-shadow: 10px 3px;margin: 10px;">
      <h3>{{item._source.title}}</h3>
      <label style="display:block;color:orange;">{{item._score}}</label>
      <p>{{item._source.short}}</p>
      <a :href="item._source.link">{{item._source.link}}</a>
      <label v-if="res.length==0" style="color:grey;">Search result empty</label>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  data: function() {
    return {
      query: '',
      res: []
    }
  },
  methods: {
    search: function() {
      var that = this;
      this.$http.get('http://localhost:5000/search', {params: {query: this.query}}).then(response => {
        console.log(response.body);
        var data = response.body;
        for (var i=0; i<data.length; i++) {
          data[i]._source['short'] = data[i]._source.art.substring(50)
        }
        that.res = data;
      })
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
