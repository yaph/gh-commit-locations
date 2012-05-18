google.load('visualization', '1', {'packages': ['geochart']});

var dataurl = 'https://docs.google.com/spreadsheet/ccc?key=0Ajfu-hBSP-VLdFlkbFpWYTBxQ3Z4Mjc4bWxtUE5zX1E ';

var settings = {
    colorSchemes: [
        ['#A50026', '#D73027', '#F46D43', '#FDAE61', '#FEE090', '#FFFFBF', '#E0F3F8', '#ABD9E9', '#74ADD1', '#4575B4', '#313695'], // diverging red to blue
        ['#FFFFCC', '#FFEDA0', '#FED976', '#FEB24C', '#FD8D3C', '#FC4E2A', '#E31A1C', '#BD0026', '#800026'], // sequential yellow to red
        ['#F7FCFD', '#E5F5F9', '#CCECE6', '#99D8C9', '#66C2A4', '#41AE76', '#238B45', '#006D2C', '#00441B'], // sequential blue to green
    ],
    colorScheme: 0,
    dataTypes: ['relative', 'absolute', 'population'],
    dataType: 0,
    maxValue: {
        'relative': 550,
        'absolute': null,
        'population': null
    },
    queryCol: {
        'relative': 'D',
        'absolute': 'B',
        'population': 'E'
    },
    queryStr: 'SELECT A, # ORDER BY # DESC',
    mapRegions: {
        'World': null,

        'Americas': '019',
        'Northern America': '021',
        'Caribbean': '029',
        'Central America': '013',
        'South America': '005',

        'Europe': '150',
        'Northern Europe': '154',
        'Western Europe': '155',
        'Eastern Europe': 151,
        'Southern Europe': '039',

        'Asia': '142',
        'Central Asia': '143',
        'Eastern Asia': '030',
        'Southern Asia': '034',
        'South-Eastern Asia': '035',
        'Western Asia': '145',

        'Africa': '002',
        'Northern Africa': '015',
        'Western Africa': '011',
        'Middle Africa': '017',
        'Eastern Africa': '014',
        'Southern Africa': '018',

        'Oceania': '009',
        'Australia and New Zealand': '053',
        'Melanesia': '054',
        'Micronesia': '057',
        'Polynesia': '061'
    },
    mapRegion: null // show world by default
};

function drawMap() {
    query = new google.visualization.Query(dataurl);
    var queryStr = settings.queryStr.replace(/#/g, settings.queryCol[settings.dataTypes[settings.dataType]]);
    query.setQuery(queryStr);
    query.send(handleQueryResponse);
}

function handleQueryResponse(response) {
    if (response.isError()) {
        alert('Error in query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
        return;
    }
    var vis = new google.visualization.GeoChart(document.getElementById('map'));
    var dataTable = response.getDataTable();
    vis.draw(dataTable, {
        colorAxis: {
            colors: settings.colorSchemes[settings.colorScheme],
            maxValue: settings.maxValue[settings.dataTypes[settings.dataType]]
        },
        datalessmapRegionColor: 'FFFFFF',
        width:900,
        height:500,
        region: settings.mapRegions[settings.mapRegion]
    });

    slide(dataTable);
}

function slide(dataTable) {
  var col = settings.queryCol[settings.dataTypes[settings.dataType]];
  var maxDataVal = Math.ceil(dataTable.D[0].c[1].v);
  var settingsVal = settings.maxValue[settings.dataTypes[settings.dataType]]
  if (null === settingsVal) {
    settingsVal = maxDataVal;
    settings.maxValue[settings.dataTypes[settings.dataType]] = maxDataVal;
  }
  $('#sliderRange').attr('max', maxDataVal);
  $('#sliderRange').attr('value', settingsVal);
  $('#sliderMax').html(maxDataVal);
  $('#sliderText').attr('value', settingsVal);
  $('#sliderRange').attr('step', Math.ceil(maxDataVal/50));
}

$(function(){
  drawMap();
  $('.mapSettings').change(function(evt){
    if ('null' !== this.value && 'selected' !== this.selected) {
      settings[this.id] = this.value;
      $('#map').empty();
      drawMap();
    };
  });
  $('#sliderRange').change(function(evt){
    settings.maxValue[settings.dataTypes[settings.dataType]] = parseInt(this.value);
    drawMap();
  });
  $('#sliderText').bind('keypress', function(evt){
    if (13 == event.which) {
      event.preventDefault();
      settings.maxValue[settings.dataTypes[settings.dataType]] = parseInt(this.value);
      drawMap();
    }
  });
});

