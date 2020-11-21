<template>
  <div class="container-fluid" id="app">
	<div class="container-fluid">
		<nav class="navbar navbar-dark fixed-top">
			<div align="left" class="navbar-brand">
				<i class="fab fa-twitter"></i>
				Twitter Polarity
			</div>
			<div align=right>
				<form v-on:submit.prevent="search" class="form-inline">
				<input class="form-control mr-sm-2" type="search" placeholder="Search" v-model="search_query">
				<button class="btn btn-light my-2" type="submit"><i class="fas fa-search"></i></button>
				</form>
			</div>
		</nav>
		<div>
			<div :key=hashtag.id v-for="hashtag in hashtags" class="row hashtag-card card">
				<div class="col-8 card-header" @click="goto(hashtag.url)">
					<h2>{{hashtag.id + ". " + hashtag.title}}</h2>
					<div class="hashtag-desc card-text">
						{{hashtag.body}}
						<br>
						Tweets:- {{hashtag.num}}
					</div>
				</div>
				<div class="col-4 card-header" data-toggle="modal" data-target="#modal">
					<h2>{{hashtag.sentiment}}</h2>
				</div>
				<app-modal :loaded="loaded"></app-modal>
			</div>
		</div>
	</div>
    
  </div>
</template>

<script>
import Graph from './Graph.vue';
export default {
name: 'App',
components: {
	'app-modal': Graph
},
data(){
	return{
		search_query: "",
		loaded: true,
		hashtags: [
			{
				id: 1,
				title: "Hashtag 1",
				sentiment: "Sentiment 1",
				url: "",
				body: "body1",
				num: "100"
			},
			{
				id: 2,
				title: "Hashtag 2",
				sentiment: "Sentiment 2",
				url: "",
				body: "body1",
				num: "100"
			},
			{
				id: 3,
				title: "Hashtag 3",
				sentiment: "Sentiment 3",
				url: "",
				body: "body1",
				num: "100"
			}
		]
	}
  },
methods:{
	goto: function(link){
		this.$http.get(link);
	},
	search: function(){
		this.$http.get('https://41138d1d5c0a.ngrok.io/polarityByDay').then(resp => {
			console.log("success");
			console.log(resp.body)
		}, resp => {
			console.log("error");
			console.log(resp)
		});
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
  color: white;
  margin-top: 60px;
}
.container-fluid, .navbar {
	background-color: rgb(21, 32, 43);
	padding-block-end: 100px;
	padding-block-start: 10px;
}
.navbar {
	flex-wrap: nowrap !important;
}
.topic {
	
}
.hashtag {
	border: 1px solid black;
	margin: 5px;
}
.hashtag-desc {
	color: rgb(136, 153, 166);
}
.hashtag-card {
	background-color: inherit !important;
	border: 1px solid white !important;
	flex-direction: inherit !important;
	margin-top: 10px;
	margin-bottom: 5px;
}
.form-inline {
	flex-flow: nowrap !important;
}
</style>
