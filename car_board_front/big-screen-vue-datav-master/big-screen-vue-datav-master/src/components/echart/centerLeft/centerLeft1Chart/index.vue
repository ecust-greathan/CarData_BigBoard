<template>
  <div>
    <!-- <Chart :cdata="cdata" /> -->
    <div ref="chart" style="width: 300px; height: 340px;" v-bind:key="cdata.seriesData[0][0]"></div>
  </div>
</template>

<script>
// import Chart from './chart.vue';
export default {
  data () {
    return {
      cdata: {
        xData: ["data1", "data2", "data3", "data4", "data5", "data6"],
        seriesData: [
          { value: 10, name: "data1" },
          { value: 5, name: "data2" },
          { value: 15, name: "data3" },
          { value: 25, name: "data4" },
          { value: 20, name: "data5" },
          { value: 35, name: "data6" }
        ]
      }
    }
  },
  components: {
    // Chart,
  },
  async mounted () {
    const res = await this.$http.get('myApp/centerLeft');
    this.$set(this.cdata, 'seriesData', res.data.data.lastPieList)
  },
  updated () {
    this.initChart();
  },
  methods: {
    initChart(){
      this.myChart = this.$echarts.init(this.$refs.chart);
      const option = {
        color: [
            "#37a2da",
            "#32c5e9",
            "#9fe6b8",
            "#ffdb5c",
            "#ff9f7f",
            "#fb7293",
            "#e7bcf3",
            "#8378ea"
          ],
          tooltip: {
            trigger: "item",
            formatter: "{a} <br/>{b} : {c} ({d}%)"
          },
          toolbox: {
            show: true
          },
          calculable: true,
          legend: {
            orient: "horizontal",
            icon: "circle",
            bottom: 0,
            x: "center",
            data: this.cdata.seriesData.map(item => item.name),
            textStyle: {
              color: "#fff"
            }
          },
          series: [
            {
              name: "销量占比",
              type: "pie",
              radius: [20, 80],
              roseType: "area",
              center: ["50%", "40%"],
              data: this.cdata.seriesData
            }
          ]
      }
      this.myChart.setOption(option);
    }
  }
}
</script>

<style lang="scss" scoped>
</style>