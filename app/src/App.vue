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
			<div v-if="search_active" class="row hashtag-card card">
				<div class="col-6 card-header" @click="goto(hashtag_search.url)">
					<h3>{{hashtag_search.name}}</h3>
					<div class="hashtag-desc card-text">
						Tweets:- {{hashtag_search.tweet_volume}}
						<div v-if="hashtag_search.promoted_content">Promoted Content</div>
					</div>
				</div>
				<div class="col-6 card-header" @click="hashtag_search.show=!hashtag_search.show">
					<line-chart class="small" :chartdata="chartdata_search" :options="options"></line-chart>
				</div>
				<bar-chart class="medium" v-if="hashtag_search.show" :chartdata="chartdataBar_search" :options="optionsBar"></bar-chart>
			</div>

			<div v-else :key=hashtag.name v-for="(hashtag, index) in hashtags" class="row hashtag-card card">
				<div class="col-6 card-header" @click="goto(hashtag.url)">
					<h3>{{hashtag.name}}</h3>
					<div class="hashtag-desc card-text">
						Tweets:- {{hashtag.tweet_volume}}
						<div v-if="hashtag.promoted_content">Promoted Content</div>
					</div>
				</div>
				<div class="col-6 card-header" @click="hashtag.show=!hashtag.show">
					<line-chart class="small" :chartdata="chartdata[index]" :options="options"></line-chart>
				</div>
				<bar-chart class="medium" v-if="hashtag.show" :chartdata="chartdataBar[index]" :options="optionsBar"></bar-chart>
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
		search_active: false,
		hashtag_search: {},
		hashtags: [],
		chartdata: [],
		chartdataBar: [],
		chartdataBar_search: [],
		chartdata_search: [],
		options: {
			responsive: true,
			maintainAspectRatio: false,
			aspectRaio: 2,
			scales: {
				xAxes: [{
					display: true,
					gridLines: {
						display: false
					},
					scaleLabel: {
						display: true,
						labelString: 'Day'
					}
				}],
				yAxes: [{
					display: true,
					gridLines: {
						display: true,
						color: 'white'
					},
					scaleLabel: {
						display: true
					}
				}]
			}
		},
		optionsBar: {
			responsive: true,
			maintainAspectRatio: false,
			aspectRaio: 2,
			title: {
				display: true,
				text: 'Sentiment Trend this week'
			},
			scales: {
				xAxes: [{
					display: true,
					gridLines: {
						display: false
					},
					scaleLabel: {
						display: true,
						labelString: 'Day'
					}
				}],
				yAxes: [{
					display: true,
					gridLines: {
						display: true,
						color: 'white'
					},
					scaleLabel: {
						display: true
					}
				}]
			}
		}
	}
  },
created(){
	let hashtags = this.hashtags;
	this.$http.get('http://0.0.0.0:5000/home/USA').then(resp => {
		return resp.json();
	})
	.then(data => hashtags = data);
	this.fetch(hashtags);
},
methods:{
	goto: function(link){
		window.location.href=link;
	},
	search: function(){
		this.search_active = true;
		this.fetch_search(this.hashtag_search);
	},
	fetch: function(hashtags){
		let pos = [], neg = [], neutral = [], hashtag, chartdataBar = [], label = [], chartdata = [], score = [];
		for(hashtag of hashtags){
			pos = [];
			neg = [];
			neutral = [];
			label = [];
			score = [];
			for(let iter of hashtag['date_polarity_counts']){
				if("1" in iter)
					pos.push(iter["1"]);
				else
					pos.push(0);
				if("-1" in iter)
					neg.push(iter["-1"]);
				else
					neg.push(0);
				if("0" in iter)
					neutral.push(iter["0"]);
				else
					neutral.push(0);
				label.push(iter["date"].substring(0,3));
				if(iter["polarity_index"] !== Infinity)
					score.push(iter["polarity_index"]);
				else
					score.push(10);
				// console.log(iter);
			}
			chartdataBar.push(
				{
				labels: label,
				datasets: [
					{
						backgroundColor: 'blue',
						borderColor: 'blue',
						data: pos,
						label: 'Positive',
						fill: false,
					},
					{
						backgroundColor: 'red',
						borderColor: 'red',
						data: neg,
						label: 'Negative',
						fill: false
					},
					{
						backgroundColor: 'yellow',
						borderColor: 'yellow',
						data: neutral,
						label: 'Neutral',
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
						fill: false,
						label: "Polarity Index"
					}
					]
				}
			)
		}
		this.chartdataBar = chartdataBar;
		this.chartdata = chartdata;
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
