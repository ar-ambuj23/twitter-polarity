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
			<div :key=hashtag.name v-for="(hashtag, index) in hashtags" class="row hashtag-card card">
				<div class="col-6 card-header" @click="goto(hashtag.url)">
					<h2>{{hashtag.name}}</h2>
					<div class="hashtag-desc card-text">
						Tweets:- {{hashtag.tweet_volume}}
						<div v-if=hashtag.promoted_content>Promoted Content</div>
					</div>
				</div>
				<div class="col-6 card-header" @click="hashtag.show=!hashtag.show">
					<line-chart class="small" :chartdata="chartdata[index]" :options="options"></line-chart>
				</div>
				<bar-chart class="medium" v-if="hashtag.show" :chartdata="chartdataBar[index]" :options="options"></bar-chart>
			</div>
		</div>
	</div>
    
  </div>
</template>

<script>
import LineChart from './LineChart.vue'
import BarChart from './BarChart.vue'
export default {
name: 'App',
components: {
	'line-chart': LineChart,
	'bar-chart': BarChart
},
data(){
	return{
		search_query: "",
		hashtags: [
			{
				"date_polarity_counts": [
					{
						"0": 2,
						"1": 2,
						"score": 1,
						"date": "Sun, 15 Nov 2020 00:00:00 GMT"
					},
					{
						"-1": 2,
						"0": 2,
						"1": 1,
						"score": 1,
						"date": "Mon, 16 Nov 2020 00:00:00 GMT"
					},
					{
						"1": 2,
						"score": 1,
						"date": "Tue, 17 Nov 2020 00:00:00 GMT"
					},
					{
						"0": 1,
						"1": 1,
						"score": 1,
						"date": "Wed, 18 Nov 2020 00:00:00 GMT"
					},
					{
						"-1": 2,
						"0": 2,
						"1": 2,
						"score": 1,
						"date": "Thu, 19 Nov 2020 00:00:00 GMT"
					},
					{
						"0": 5,
						"1": 5,
						"score": 1,
						"date": "Fri, 20 Nov 2020 00:00:00 GMT"
					},
					{
						"-1": 4,
						"0": 3,
						"1": 3,
						"score": 1,
						"date": "Sat, 21 Nov 2020 00:00:00 GMT"
					}
				],
				"name": "#UFC255",
				"promoted_content": true,
				"query": "%23UFC255",
				"tweet_volume": 17993,
				"url": "http://twitter.com/search?q=%23UFC255",
				"show": false
			},
			{
				"date_polarity_counts": [
					{
						"-1": 1,
						"0": 2,
						"1": 7,
						"score": 1,
						"date": "Sun, 15 Nov 2020 00:00:00 GMT"
					},
					{
						"-1": 2,
						"0": 2,
						"1": 6,
						"score": 1,
						"date": "Mon, 16 Nov 2020 00:00:00 GMT"
					},
					{
						"-1": 2,
						"0": 3,
						"1": 5,
						"score": 1,
						"date": "Tue, 17 Nov 2020 00:00:00 GMT"
					},
					{
						"-1": 1,
						"0": 4,
						"1": 5,
						"score": 1,
						"date": "Wed, 18 Nov 2020 00:00:00 GMT"
					},
					{
						"0": 4,
						"1": 6,
						"score": 1,
						"date": "Thu, 19 Nov 2020 00:00:00 GMT"
					},
					{
						"0": 4,
						"1": 6,
						"score": 1,
						"date": "Fri, 20 Nov 2020 00:00:00 GMT"
					},
					{
						"-1": 3,
						"0": 5,
						"1": 2,
						"score": 1,
						"date": "Sat, 21 Nov 2020 00:00:00 GMT"
					}
				],
				"name": "Northwestern",
				"promoted_content": null,
				"query": "Northwestern",
				"tweet_volume": 12925,
				"url": "http://twitter.com/search?q=Northwestern",
				"show": false
			},
		],
		chartdata: [],
		chartdataBar: [],
		options: {
			responsive: true,
			maintainAspectRatio: false,
			aspectRaio: 2
		}
	}
  },
created(){
	// this.hashtags ;
	// get hashtags from endpt 1
	let pos = [], neg = [], neutral = [], hashtag, chartdataBar = [], label = [], chartdata = [], score = [];
	for(hashtag of this.hashtags){
		pos = [];
		neg = [];
		neutral = [];
		label = [];
		score = [];
		for(let iter of hashtag['date_polarity_counts']){
			pos.push(iter["1"]);
			neg.push(iter["-1"]);
			neutral.push(iter["0"]);
			label.push(iter["date"].substring(0,3));
			score.push(iter["score"]);
			console.log(iter);
		}
		chartdataBar.push(
			{
			labels: label,
			datasets: [
				{
					backgroundColor: 'blue',
					borderColor: 'blue',
					data: pos,
					fill: false
				},
				{
					backgroundColor: 'red',
					borderColor: 'red',
					data: neg,
					fill: false
				},
				{
					backgroundColor: 'yellow',
					borderColor: 'yellow',
					data: neutral,
					fill: false
				}
			]
			}
		);
		chartdata.push(
			{
				labels: label,
				datasets: [
				{
					backgroundColor: 'blue',
					borderColor: 'blue',
					data: score,
					fill: false
				}
				]
			}
		)
	}
	this.chartdataBar = chartdataBar;
	this.chartdata = chartdata;
	console.log(pos, neg, neutral);
},
methods:{
	goto: function(link){
		window.location.href=link;
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
.small {
	width: 250px;
	height: 150px;
}
.medium {
	width: 550px;
	height: 250px;
}
</style>
