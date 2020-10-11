<template>
  <div id="app">
    <h1>News Aggregator</h1>
    <input placeholder="Start your search" v-model="query"/>
    <button @click="search">search</button>
    <div v-for="item in res" :key="item._id" style="box-shadow: 0px 1px;margin: 85px;text-align:left; line-height:37.8px;">
      <a :href="item._source.link">{{item._source.title}}</a>
      <p>{{item._source.short}}</p>
      <label v-if="res.length==0" style="color:grey;">Search result empty</label>

      <el-button @click="search_keyword">{{keyword}}</el-button>

    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  data: function() {
    return {
      query: '',
      res: [],
      keyword:''
    }
  },
  methods: {
    search: function() {
      var that = this;
      this.$http.get('http://localhost:5000/search', {params: {query: this.query}}).then(response => {
        console.log(response.body);
        var data = response.body;
        for (var i=0; i<data.length; i++) {
          data[i]._source['short'] = data[i]._source.art
        }
        that.res = data;
        that.keyword = this.query;
      })
    }

  ,

  search_keyword: function() {
      var that = this;
      this.$http.get('http://localhost:5000/search', {params: {query: this.keyword}}).then(response => {
        console.log(response.body);
        var data = response.body;
        for (var i=0; i<data.length; i++) {
          data[i]._source['short'] = data[i]._source.art
        }
        that.res = data;
        that.keyword = this.query;
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

a {
    text-decoration:none;
    font-size:25px;
    outline:none;
    text-align:center;
    width:50px;
    line-height:35px;
    cursor: pointer;
}

el-button {
  color:cyan;
  cursor:pointer;
  font-weight:870;
}
</style>
