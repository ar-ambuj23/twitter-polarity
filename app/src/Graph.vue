<template>
    <div class="modal fade" id="modal">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Demo</h5>
                    <line-chart v-if="loaded" :chartdata="chartdata" :options="options"></line-chart>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import LineChart from './LineChart.vue'
export default {
    components: {
        'line-chart': LineChart
    },
    props: {
        loaded:{
            type:Boolean
        }
    },
    data(){
        return{
            chartdata: {
                labels: ['Jan','Feb'],
                datasets: [
                    {
                        label: 'Data One',
                        data: [10,20]
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        };
    }
}
</script>

<style>
.modal-content {
    background-color: rgb(21, 32, 43) !important;
}
</style>