const entries = [
    {
        id: "digital-twin-root",
        category: "meta-components",
        addComponent: {
            title: 'New Digital Twin Root',
            description: 'Adds a new Digital Twin root item',
        },
        component: {
            title: "Digital Twin Root"
        },
        icon: 'assets/twin.svg',
        iconColor: 'assets/twin-blue.svg'
    },
    {
        id: "digital-twin-child",
        category: "meta-components",
        addComponent: {
            title: 'Digital Twin Child',
            description: 'Adds a new Digital Twin child item',
        },
        component: {
            title: "Digital Twin Child"
        },
        icon: 'assets/twin.svg',
        iconColor: 'assets/twin-blue.svg'
    },
    {
        id: "sensor-turbine-h",
        category: "sensor",
        addComponent: {
            title: 'Turbine (Horizontal)',
            description: 'Represents the rotation value of the Horizontal Shaft in the Wind Turbine',
        },
        component: {
            title: "Turbine (Horizontal)",
            description: "Represents the rotation value of the Horizontal Shaft in the Wind Turbine"
        },
        measures: [
            {
                nameKey: "rotationAngle",
                value: {
                    type: "continuous",
                    dataType: "int",
                    lowerLimit: 0,
                    upperLimit: 360
                }
            },
            {
                nameKey: "rotationSpeed",
                value: {
                    type: "continuous",
                    dataType: "double",
                    lowerLimit: 0,
                    upperLimit: 100
                }
            }
        ],
        icon: 'assets/sensor.svg',
        iconColor: 'assets/sensor-blue.svg'
    },
    {
        id: "sensor-turbine-v",
        category: "sensor",
        addComponent: {
            title: 'Turbine (Vertical)',
            description: 'Represents the rotation value of the Vertical Shaft in the Wind Turbine',
        },
        component: {
            title: "Turbine (Vertical)",
            description: "Represents the rotation value of the Vertical Shaft in the Wind Turbine"
        },
        measures: [
            {
                nameKey: "rotationAngle",
                value: {
                    type: "continuous",
                    dataType: "int",
                    lowerLimit: 0,
                    upperLimit: 360
                }
            },
            {
                nameKey: "rotationSpeed",
                value: {
                    type: "continuous",
                    dataType: "double",
                    lowerLimit: 0,
                    upperLimit: 100
                }
            }
        ],
        icon: 'assets/sensor.svg',
        iconColor: 'assets/sensor-blue.svg'
    },
    {
        id: "sensor-temperature",
        category: "sensor",
        addComponent: {
            title: 'Temperature',
            description: 'Measures Temperature',
        },
        component: {
            title: "Temperature",
            description: "Measures Temperature"
        },
        icon: 'assets/sensor.svg',
        iconColor: 'assets/sensor-blue.svg'
    },
    {
        id: "sensor-proximity",
        category: "sensor",
        addComponent: {
            title: 'Proximity',
            description: 'Measure Proximity',
        },
        component: {
            title: "Proximity",
            description: "Measure Proximity"
        },
        icon: 'assets/sensor.svg',
        iconColor: 'assets/sensor-blue.svg'
    },
    {
        id: "sensor-accelerometer",
        category: "sensor",
        addComponent: {
            title: 'Accelerometer',
            description: 'Measures Accelerometer',
        },
        component: {
            title: "Accelerometer",
            description: "Measures Accelerometer"
        },
        icon: 'assets/sensor.svg',
        iconColor: 'assets/sensor-blue.svg'
    },
    {
        id: "sensor-light",
        category: "sensor",
        addComponent: {
            title: 'Light',
            description: 'Measures Light',
        },
        component: {
            title: "Light",
            description: "Measures Light"
        },
        icon: 'assets/sensor.svg',
        iconColor: 'assets/sensor-blue.svg'
    },
    {
        id: "api-weather-temperature",
        category: "api",
        addComponent: {
            title: 'New Weather API (Temperature)',
            description: 'Returns the temperature at this moment (C)',
        },
        component: {
            title: "Weather API (Temperature)",
            description: "Returns the temperature at this moment (C)"
        },
        measures: [
            {
                nameKey: "temperature",
                value: {
                    type: "continuous",
                    dataType: "double",
                    lowerLimit: -20,
                    upperLimit: 40
                }
            }
        ],
        icon: 'assets/weather.svg',
        iconColor: 'assets/weather-blue.svg'
    },
    {
        id: "api-weather-wind",
        category: "api",
        addComponent: {
            title: 'New Weather API (Wind Speed)',
            description: 'Returns the wind speed at this moment (kmh)',
        },
        component: {
            title: "Weather API (Wind Speed)",
            description: "Returns the wind speed at this moment (kmh)"
        },
        measures: [
            {
                nameKey: "windSpeed",
                value: {
                    type: "continuous",
                    dataType: "double",
                    lowerLimit: 0,
                    upperLimit: 90
                }
            },
            {
                nameKey: "windOrientation",
                value: {
                    type: "discrete",
                    dataType: "enum",
                    values: [ "N", "NE", "E", "SE", "S", "SW", "W", "NW" ]
                }
            }
        ],
        icon: 'assets/weather-wind.svg',
        iconColor: 'assets/weather-wind-blue.svg'
    }
];

const toggleLeftCard = () => {
    $("#leftcard").toggle();

    if ($("#leftcard").is(":visible")) {
        $("#closecard").css("margin-left", "363px");
        $("#closecard").html("<img src='assets/closeleft.svg' />");
    } else {
        $("#closecard").css("margin-left", "0px");
        $("#closecard").html("<img src='assets/openright.svg' />");
    }
};

const generateBlockHtml = (id, title, description, icon) => {
    return `
    <div class="blockelem create-flowy noselect">
        <input type="hidden" name="blockelemtype" class="blockelemtype" value="${id}">
        <div class="grabme">
            <img src="assets/grabme.svg"></div>
            <div class="blockin">
                <div class="blockico"><span></span><img src="${icon}"></div>
                <div class="blocktext">
                <p class="blocktitle">${title}</p>
                ${description && `<p class="blockdesc">${description}</p>`}
            </div>
        </div>
    </div>
    `
}

// {
//     nameKey: "windSpeed",
//     value: {
//         type: "continuous",
//         dataType: "double",
//         lowerLimit: 0,
//         upperLimit: 90
//     }
// },
// {
//     nameKey: "windOrientation",
//     value: {
//         type: "discrete",
//         dataType: "enum",
//         values: [ "N", "NE", "E", "SE", "S", "SW", "W", "NW" ]
//     }
// }
const generateBlockDiagramMeasuresHtml = (measurement) => {
    switch (measurement.value.type) {
        case "continuous":
            return `${measurement.value.dataType} ${measurement.nameKey} [${measurement.value.lowerLimit} ${measurement.value.upperLimit}]`;
        case "discrete":
            return `${measurement.value.dataType} ${measurement.nameKey} [${measurement.value.values.join(', ')}]`;
        default:
            return "Not-Implemented"
    }
};

const generateBlockDiagramHtml = (id, title, description, measures = [], icon) => {
    return `
    <div class='blockyleft'>
        <img src='${icon}'>
        <p class='blockyname'>${title}</p>
    </div>
    <div class='blockyright'><img src='assets/more.svg'></div>

    ${
        description ? `
        <div class='blockydiv'></div>
        <p class="blockdesc">${description}</p>
        ` : ""
    }
    ${
        measures ? `
            <ul>
                ${measures.map(i => `<li>${generateBlockDiagramMeasuresHtml(i)}</li>`).join('')}
            </ul>
        ` : ""
    }
    `;
}

function initBlocklist(entryKey) {
    let components = entries.filter(i => i.category == entryKey);

    html = '';
    for (let i in components) {
        html += generateBlockHtml(components[i].id, components[i].addComponent.title, components[i].addComponent.description, components[i].icon);
    }

    $("#blocklist").html(html);
}

$(document).ready(function(){
    var rightcard = false;
    var tempblock;
    var tempblock2;
    
    initBlocklist("meta-components");

    flowy($("#canvas"), drag, release, snapping);
    
    function snapping(drag, first) {
        drag.children(".grabme").remove();
        drag.children(".blockin").remove();

        const componentId = drag.children(".blockelemtype").val();
        const componentInfo = entries.filter(i => i.id == componentId)[0];

        drag.append(generateBlockDiagramHtml(componentInfo.id, componentInfo.component.title, componentInfo.component.description, componentInfo.measures, componentInfo.iconColor));
        return true;
    }
    
    function drag(block) {
        block.addClass("blockdisabled");
        tempblock2 = block;
    }
    function release() {
        tempblock2.removeClass("blockdisabled");
    }
    $(document).on("click", ".navdisabled", function(){
        $(".navactive").addClass("navdisabled");
        $(".navactive").removeClass("navactive");
        $(this).addClass("navactive");
        $(this).removeClass("navdisabled");

        // Handle clicking Meta Blocks component....
        let entryKey = $(this).attr("id");
        initBlocklist(entryKey);
    });
    $("#close").click(function(){
       if (rightcard) {
           rightcard = false;
           $("#properties").removeClass("expanded");
           setTimeout(function(){
                $("#propwrap").removeClass("itson"); 
           }, 300);
            tempblock.removeClass("selectedblock");
       } 
    });
$("#removeblock").on("click", function(){
 flowy.deleteBlocks();
});
$(document).on("mousedown touchstart", ".block", function (event) {
  $(document).on("mouseup mousemove", ".block", function handler(event) {
    if (event.type === "mouseup") {
      if (!rightcard) {
            tempblock = $(this);
           rightcard = true;
           $("#properties").addClass("expanded");
        $("#propwrap").addClass("itson");
            tempblock.addClass("selectedblock");
       } 
    }
    $(document).off("mouseup mousemove", handler);
  });
});
});