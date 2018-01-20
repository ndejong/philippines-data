
var map;
var heatmap;
var data;
var data_mvc;
//var regions_active = getAllRegions(data);
var regions_active = [];

document.getElementById('floating-panel-title').textContent="density";

function initMap() {

    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 7,
        center: {lat: 11.5528816, lng: 122.740723},
        mapTypeId: 'terrain'
    });

    data_mvc = new google.maps.MVCArray(getActiveRegionData(regions_active));

    heatmap = new google.maps.visualization.HeatmapLayer({
        data: data_mvc,
        map: map,
        radius: 50,
        opacity: 0.75
    });

}

function toggleRegion(region) {
    if (regions_active.indexOf(region) === -1) {
        regions_active.push(region)
    } else {
        regions_active.splice(regions_active.indexOf(region), 1)
    }

    data_mvc.clear()
    var active_region_data = getActiveRegionData(regions_active)
    for(active_region_data_index in active_region_data){
        data_mvc.push({
            location: active_region_data[active_region_data_index]['location'],
            weight: active_region_data[active_region_data_index]['weight']
        });
    }

}

function getAllRegions(all_data) {
    var regions = []
    for (var key in all_data) {
        if (regions.indexOf(all_data[key]['region']) === -1){
            regions.push(all_data[key]['region']);
        }
    }
    return regions
}

function getActiveRegionData() {
    var active_region_data = []
    for(var data_index in data) {
        if(regions_active.indexOf(data[data_index]['region']) >= 0) {
            active_region_data.push({
                location: new google.maps.LatLng(
                    data[data_index]['google_geocode'][0]['geometry']['location']['lat'],
                    data[data_index]['google_geocode'][0]['geometry']['location']['lng'],
                ),
                weight: parseFloat(data[data_index]['population_density'])
            })
        }
    }
    return active_region_data
}

function changeGradient() {
    var gradient = [
    'rgba(0, 0, 0, 0)',
    'rgba(0, 0, 0, 1)',
    'rgba(0, 0, 0, 1)',
    'rgba(0, 0, 0, 1)',
    'rgba(0, 0, 0, 1)',
    'rgba(0, 0, 0, 1)',
    'rgba(0, 0, 0, 1)',
    'rgba(0, 0, 0, 1)',
    'rgba(0, 0, 0, 1)',
    'rgba(0, 0, 0, 1)',
    'rgba(0, 0, 0, 1)',
    'rgba(0, 0, 0, 1)',
    'rgba(0, 0, 0, 1)',
    'rgba(0, 0, 0, 1)',
    ];
    heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
}

function toggleButtonClass(this_element) {
    if(this_element.className == 'active') {
        this_element.className = ''
    } else {
        this_element.className = 'active'
    }
}
