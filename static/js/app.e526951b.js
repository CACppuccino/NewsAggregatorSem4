(function(e){function t(t){for(var n,a,c=t[0],s=t[1],i=t[2],p=0,f=[];p<c.length;p++)a=c[p],Object.prototype.hasOwnProperty.call(o,a)&&o[a]&&f.push(o[a][0]),o[a]=0;for(n in s)Object.prototype.hasOwnProperty.call(s,n)&&(e[n]=s[n]);l&&l(t);while(f.length)f.shift()();return u.push.apply(u,i||[]),r()}function r(){for(var e,t=0;t<u.length;t++){for(var r=u[t],n=!0,c=1;c<r.length;c++){var s=r[c];0!==o[s]&&(n=!1)}n&&(u.splice(t--,1),e=a(a.s=r[0]))}return e}var n={},o={app:0},u=[];function a(t){if(n[t])return n[t].exports;var r=n[t]={i:t,l:!1,exports:{}};return e[t].call(r.exports,r,r.exports,a),r.l=!0,r.exports}a.m=e,a.c=n,a.d=function(e,t,r){a.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},a.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},a.t=function(e,t){if(1&t&&(e=a(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(a.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)a.d(r,n,function(t){return e[t]}.bind(null,n));return r},a.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return a.d(t,"a",t),t},a.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},a.p="/";var c=window["webpackJsonp"]=window["webpackJsonp"]||[],s=c.push.bind(c);c.push=t,c=c.slice();for(var i=0;i<c.length;i++)t(c[i]);var l=s;u.push([0,"chunk-vendors"]),r()})({0:function(e,t,r){e.exports=r("56d7")},"034f":function(e,t,r){"use strict";var n=r("85ec"),o=r.n(n);o.a},1:function(e,t){},"56d7":function(e,t,r){"use strict";r.r(t);r("e260"),r("e6cf"),r("cca6"),r("a79d");var n=r("2b0e"),o=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{attrs:{id:"app"}},[r("h1",[e._v("News Aggregator Demo")]),r("input",{directives:[{name:"model",rawName:"v-model",value:e.query,expression:"query"}],attrs:{placeholder:"whats your problem"},domProps:{value:e.query},on:{input:function(t){t.target.composing||(e.query=t.target.value)}}}),r("button",{on:{click:e.search}},[e._v("search")]),e._l(e.res,(function(t){return r("div",{key:t._id,staticStyle:{"box-shadow":"10px 3px",margin:"10px"}},[r("h3",[e._v(e._s(t._source.title))]),r("label",{staticStyle:{display:"block",color:"orange"}},[e._v(e._s(t._score))]),r("p",[e._v(e._s(t._source.short))]),r("a",{attrs:{href:t._source.link}},[e._v(e._s(t._source.link))]),0==e.res.length?r("label",{staticStyle:{color:"grey"}},[e._v("Search result empty")]):e._e()])}))],2)},u=[],a={name:"App",data:function(){return{query:"",res:[]}},methods:{search:function(){var e=this;this.$http.get("http://localhost:5000/search",{params:{query:this.query}}).then((function(t){console.log(t.body);for(var r=t.body,n=0;n<r.length;n++)r[n]._source["short"]=r[n]._source.art.substring(50);e.res=r}))}}},c=a,s=(r("034f"),r("2877")),i=Object(s["a"])(c,o,u,!1,null,null,null),l=i.exports,p=r("28dd");n["a"].config.productionTip=!1,n["a"].use(p["a"]),new n["a"]({render:function(e){return e(l)}}).$mount("#app")},"85ec":function(e,t,r){}});
//# sourceMappingURL=app.e526951b.js.map