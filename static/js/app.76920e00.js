(function(e){function t(t){for(var o,i,s=t[0],c=t[1],u=t[2],p=0,h=[];p<s.length;p++)i=s[p],Object.prototype.hasOwnProperty.call(n,i)&&n[i]&&h.push(n[i][0]),n[i]=0;for(o in c)Object.prototype.hasOwnProperty.call(c,o)&&(e[o]=c[o]);l&&l(t);while(h.length)h.shift()();return a.push.apply(a,u||[]),r()}function r(){for(var e,t=0;t<a.length;t++){for(var r=a[t],o=!0,s=1;s<r.length;s++){var c=r[s];0!==n[c]&&(o=!1)}o&&(a.splice(t--,1),e=i(i.s=r[0]))}return e}var o={},n={app:0},a=[];function i(t){if(o[t])return o[t].exports;var r=o[t]={i:t,l:!1,exports:{}};return e[t].call(r.exports,r,r.exports,i),r.l=!0,r.exports}i.m=e,i.c=o,i.d=function(e,t,r){i.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},i.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(e,t){if(1&t&&(e=i(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(i.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)i.d(r,o,function(t){return e[t]}.bind(null,o));return r},i.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return i.d(t,"a",t),t},i.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},i.p="/";var s=window["webpackJsonp"]=window["webpackJsonp"]||[],c=s.push.bind(s);s.push=t,s=s.slice();for(var u=0;u<s.length;u++)t(s[u]);var l=c;a.push([0,"chunk-vendors"]),r()})({0:function(e,t,r){e.exports=r("56d7")},"034f":function(e,t,r){"use strict";var o=r("85ec"),n=r.n(o);n.a},1:function(e,t){},"56d7":function(e,t,r){"use strict";r.r(t);r("e260"),r("e6cf"),r("cca6"),r("a79d");var o=r("2b0e"),n=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{attrs:{id:"app"}},[r("h1",[e._v("News Aggregator")]),r("br"),r("input",{directives:[{name:"model",rawName:"v-model",value:e.query,expression:"query"}],attrs:{placeholder:"Start your search"},domProps:{value:e.query},on:{input:function(t){t.target.composing||(e.query=t.target.value)}}}),r("button",{on:{click:e.origin_search}},[e._v("accurate_search")]),r("button",{on:{click:e.search}},[e._v("associative_search")]),r("br"),r("br"),r("br"),r("label",{staticStyle:{color:"grey"}},[e._v("Search spent intotal ")]),r("label",{staticStyle:{color:"grey"}},[e._v(e._s(e.timetotal))]),r("label",{staticStyle:{color:"grey"}},[e._v(" second.")]),r("br"),e._l(e.res,(function(t){return r("div",{key:t._id,staticStyle:{"box-shadow":"0px 1px",margin:"85px","text-align":"left","line-height":"37.8px"}},[r("a",{attrs:{href:t._source.link}},[e._v(e._s(t._source.title))]),r("p",[e._v(e._s(t._source.short))]),0==e.res.length?r("label",{staticStyle:{color:"grey"}},[e._v("Search result empty")]):e._e(),r("el-button",{on:{click:e.search_keyword}},[e._v(e._s(e.keyword))])],1)}))],2)},a=[],i={name:"App",data:function(){return{query:"",res:[],keyword:"",timetotal:0}},methods:{search:function(){var e=this,t=this,r=Date.now();this.$http.get("https://anu.jkl.io/search",{params:{query:this.query}}).then((function(o){var n=Date.now();t.timetotal=(n-r)/1e3,console.log(o.body);for(var a=o.body,i=0;i<a.length;i++)a[i]._source["short"]=a[i]._source.art;t.res=a,t.keyword=e.query}))},search_keyword:function(){var e=this,t=this,r=Date.now();this.$http.get("https://anu.jkl.io/search",{params:{query:this.keyword}}).then((function(o){var n=Date.now();t.timetotal=(n-r)/1e3,console.log(o.body);for(var a=o.body,i=0;i<a.length;i++)a[i]._source["short"]=a[i]._source.art;t.res=a,t.keyword=e.query}))},origin_search:function(){var e=this,t=this,r=Date.now();this.$http.get("https://anu.jkl.io/origin_search",{params:{query:this.query}}).then((function(o){var n=Date.now();t.timetotal=(n-r)/1e3,console.log(o.body);for(var a=o.body,i=0;i<a.length;i++)a[i]._source["short"]=a[i]._source.art;t.res=a,t.keyword=e.query}))}}},s=i,c=(r("034f"),r("2877")),u=Object(c["a"])(s,n,a,!1,null,null,null),l=u.exports,p=r("28dd");o["a"].config.productionTip=!1,o["a"].use(p["a"]),o["a"].component("thebutton",l),new o["a"]({render:function(e){return e(l)}}).$mount("#app")},"85ec":function(e,t,r){}});
//# sourceMappingURL=app.76920e00.js.map