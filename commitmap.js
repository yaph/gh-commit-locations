var query = null;
var dataurl = 'https://docs.google.com/spreadsheet/ccc?key=0Ajfu-hBSP-VLdFlkbFpWYTBxQ3Z4Mjc4bWxtUE5zX1E ';

var settings = {
    colorschemes: [
//        ['purple', 'darkred', 'red', 'orange', 'yellow', 'lightgreen', 'green'],
        ['#F7FCFD', '#E5F5F9', '#CCECE6', '#99D8C9', '#66C2A4', '#41AE76', '#238B45', '#006D2C', '#00441B'], // sequential
        ['#FFFFCC', '#FFEDA0', '#FED976', '#FEB24C', '#FD8D3C', '#FC4E2A', '#E31A1C', '#BD0026', '#800026'], // sequential
        ['#A50026', '#D73027', '#F46D43', '#FDAE61', '#FEE090', '#FFFFBF', '#E0F3F8', '#ABD9E9', '#74ADD1', '#4575B4', '#313695'], // divering red to blue
    ],
    colorscheme: 2,
    types: ['relative', 'absolute'],
    type: 0,
    maxValue: {
        'relative': 550,
        'absolute': 500000
    },
    query: {
        'relative': 'SELECT A,D ORDER BY D DESC',
        'absolute': 'SELECT A,B ORDER BY B DESC'
    },
    regions: {
        'World': null,
        'Africa': '002',
        'Americas': '019',
        'Asia': '142',
        'Europe': '150',
        'Oceania': '009'
    },
    region: 'World' // show world by default
};

var mapOptions = {
    colorAxis: {
        colors: settings.colorschemes[settings.colorscheme],
        maxValue: settings.maxValue[settings.types[settings.type]]
    },
    datalessRegionColor: 'FFFFFF',
    width:900,
    height:500,
    region: settings.regions[settings.region]
};

google.load('visualization', '1', {'packages': ['geochart']});
google.setOnLoadCallback(drawMap);

function drawMap() {
    if (null === query) {
      query = new google.visualization.Query(dataurl);
    }
    query.setQuery(settings.query[settings.types[settings.type]]);
    query.send(handleQueryResponse);
}

function handleQueryResponse(response) {
    if (response.isError()) {
        alert('Error in query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
        return;
    }
    var vis = new google.visualization.GeoChart(document.getElementById('map'));
    vis.draw(response.getDataTable(), mapOptions);
}
