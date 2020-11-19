<template>
  <div class="container" id="app">
    <div class="row">
		<div class="topic col col-6">
			<h1> Top Trends </h1>
			<div :key=hashtag.id v-for="hashtag in hashtags">
				<h3>{{hashtag.title}}</h3>
			</div>
		</div>
		<div class="topic col col-6">
			<h1> Sentiment </h1>
			<div :key=hashtag.id v-for="hashtag in hashtags">
				<h3>{{hashtag.sentiment}}</h3>
			</div>
		</div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  data(){
	return{
		hashtags: [
			{
				id: 1,
				title: "Hashtag 1",
				sentiment: "Sentiment 1"
			},
			{
				id: 2,
				title: "Hashtag 2",
				sentiment: "Sentiment 2"
			},
			{
				id: 3,
				title: "Hashtag 3",
				sentiment: "Sentiment 3"
			}
		]
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
.container-fluid {
	background-color: coral;
}
.topic {
	background-color: coral;
	border: 2px solid black;
}
.hashtag {
	border: 1px solid black;
	margin: 5px;
}
</style>
