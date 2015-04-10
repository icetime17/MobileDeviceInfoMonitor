
// 路径配置
require.config({
    paths: {
        echarts: 'http://echarts.baidu.com/build/dist'
    }
});


app.controller("battery", ["$scope", "$http", function($scope, $http){

	console.log("battery");

	$scope.gv = {
		'batteryData'	: {},
		'devices'		: [],
		'chosedDevice'	: 'TA iPhone 5',
	};

	$scope.getbatteryData = function() {
		$http({
				method: 'GET',
				url: '/batteryLevel/level'
			}).
			success(function(data, status) {
				$scope.gv.batteryData = data.data;
				// for (var d in $scope.gv.batteryData) {
				// 	$scope.gv.devices.push(d);
				// }

				var device = "TA iPhone 5";
				var timeArray = [];
				var batteryArray = [];
				var batteries = $scope.gv.batteryData[device]['battery'];
				for (var i=0; i<=batteries.length-1;i++) {
					timeArray.push(batteries[i][0]);
					batteryArray.push(batteries[i][1]);
				};
				$scope.drawLineEChart('batteryChart_5', timeArray, batteryArray);

				var device = "TA iPhone 5s";
				var timeArray = [];
				var batteryArray = [];
				var batteries = $scope.gv.batteryData[device]['battery'];
				for (var i=0; i<=batteries.length-1;i++) {
					timeArray.push(batteries[i][0]);
					batteryArray.push(batteries[i][1]);
				};
				$scope.drawLineEChart('batteryChart_5s', timeArray, batteryArray);

			}).
			error(function(data, status) {
				console.log(status);
			});
	}

	$scope.drawLineEChart = function(chartId, xValue, yValue) {
		require(
		    [
		        'echarts',
		        'echarts/chart/line',
		    ],
		    function (ec) {
		        var myChart = ec.init(document.getElementById(chartId)); 
		        myChart.setOption({
		            tooltip: {
		                trigger: 'axis'
		            },
		            legend: {
		                data:['Battery Level']
		            },
		            toolbox: {
		            	show: true,
		            	feature: {
		            		mark: {show: true},
		            		dataView: {show: true, readOnly: false},
		            		magicType: {show: true, type: ['line']},
		            		restore: {show: true},
		            		saveAsImage: {show: true}
		            	}
		            },
		            xAxis : [
		                {
		                    type : 'category',
		                    data : xValue
		                }
		            ],
		            yAxis : [
		                {
		                    type : 'value',
		                    splitArea : {show: true}
		                }
		            ],
		            series : [
		                {
		                    name: 'Battery Level',
		                    type: 'line',
		                    data: yValue,
		                }
		            ]
		        });
		    }
		);
	}


	// executing while loading

	$scope.getbatteryData();

}]);
