const request = require("request-promise");

module.exports = {
    test: function(){
        return "Hello";
    },
    today_api: async function(key_index){
        const response = await request.get("https://covid19.th-stat.com/api/open/today")
        const response_json = JSON.parse(response);
        return response_json[key_index];
    },
    today_api2: async function(key_index){
        const response = await request.get("https://covid19.th-stat.com/api/open/cases/sum")
        const response_json = JSON.parse(response);
        return response_json.Province[key_index];
    },
    overview_command: function(key_index){
        var overview_array = ["Confirmed", "Recovered", "Hospitalized", "Deaths", "NewConfirmed", "NewRecovered", "NewHospitalized", "NewDeaths"]
        return overview_array.includes(key_index)
    },
    province: function(key_index){
        var province_th_array = [
            'Krabi',
            'Bangkok',
            'Kanchanaburi',
            'Kalasin',
            'Kamphaengphet',
            'Khonkaen',
            'Chanthaburi',
            'Chachoengsao',
            'Chonburi',
            'Chainat',
            'Chaiyaphum',
            'Chumphon',
            'Chiangrai',
            'Chiangmai',
            'Trang',
            'Trat',
            'Tak',
            'Nakhonnayok',
            'Nakhonpathom',
            'Nakhonphanom',
            'Nakhonratchasima',
            'Nakhonsithammarat',
            'Nakhonsawan',
            'Nonthaburi',
            'Narathiwat',
            'Nan',
            'Buriram',
            'Pathumthani',
            'Prachuapkhirikhan',
            'Prachinburi',
            'Pattani',
            'Ayutthaya',
            'Phayao',
            'Phangnga',
            'Phatthalung',
            'Phichit',
            'Phitsanulok',
            'Phetchaburi',
            'Phetchabun',
            'Phrae',
            'Phuket',
            'Mahasarakham',
            'Mukdahan',
            'Maehongson',
            'Yasothon',
            'Yala',
            'roiet',
            'Ranong',
            'Rayong',
            'Ratchaburi',
            'Lopburi',
            'Loei',
            'Lampang',
            'Lamphun',
            'Sisaket',
            'Sakonnakhon',
            'Songkhla',
            'Satun',
            'Samutprakan',
            'Samutsongkhram',
            'Samutsakhon',
            'Sakaeo',
            'Saraburi',
            'Singburi',
            'Sukhothai',
            'Suphanburi',
            'Suratthani',
            'Surin',
            'Nongkhai',
            'Nongbualamphu',
            'Angthong',
            'Amnatcharoen',
            'Udonthani',
            'Uttaradit',
            'Uthaithani',
            'Ubonratchathani'
        ]
        return province_th_array.includes(key_index);
    }

}