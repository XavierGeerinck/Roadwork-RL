const entries = {
    "meta-components": [
        {
            title: 'New Digital Twin Root',
            description: 'Adds a new Digital Twin root item',
            icon: 'assets/database.svg'
        },
        {
            title: 'New Digital Twin Child',
            description: 'Adds a new Digital Twin child item',
            icon: 'assets/database.svg'
        }
    ],
    "sensors": [
        {
            title: 'New Database entry',
            description: 'Adds a new entry to a specified database',
            icon: 'assets/database.svg'
        },
        {
            title: 'Update Database',
            description: 'Lorem Ipsum .....',
            icon: 'assets/database.svg'
        },
        {
            title: 'Performan an Action',
            description: 'Lorem Ipsum .....',
            icon: 'assets/action.svg'
        },
        {
            title: 'make a tweet',
            description: 'Lorem Ipsum .....',
            icon: 'assets/twitter.svg'
        }
    ]
};

const generateBlockHtml = (title, description, icon) => {
    return `
    <div class="blockelem create-flowy noselect">
        <input type="hidden" name="blockelemtype" class="blockelemtype" value="5">
        <div class="grabme">
            <img src="assets/grabme.svg"></div>
            <div class="blockin">
                <div class="blockico"><span></span><img src="${icon}"></div>
                <div class="blocktext">
                <p class="blocktitle">${title}</p>
                <p class="blockdesc">${description}</p>
            </div>
        </div>
    </div>
    `
}

$(document).ready(function(){
    var rightcard = false;
    var tempblock;
    var tempblock2;
    $("#blocklist").html('<div class="blockelem create-flowy noselect" data-test="yayyy"><input type="hidden" name="blockelemtype" class="blockelemtype" value="1"><div class="grabme"><img src="assets/grabme.svg"></div><div class="blockin">                  <div class="blockico"><span></span><img src="assets/eye.svg"></div><div class="blocktext">                        <p class="blocktitle">New visitor</p><p class="blockdesc">Triggers when somebody visits a specified page</p>        </div></div></div><div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="2"><div class="grabme"><img src="assets/grabme.svg"></div><div class="blockin">                    <div class="blockico"><span></span><img src="assets/action.svg"></div><div class="blocktext">                        <p class="blocktitle">Action is performed</p><p class="blockdesc">Triggers when somebody performs a specified action</p></div></div></div><div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="3"><div class="grabme"><img src="assets/grabme.svg"></div><div class="blockin">                    <div class="blockico"><span></span><img src="assets/time.svg"></div><div class="blocktext">                        <p class="blocktitle">Time has passed</p><p class="blockdesc">Triggers after a specified amount of time</p>          </div></div></div><div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="4"><div class="grabme"><img src="assets/grabme.svg"></div><div class="blockin">                    <div class="blockico"><span></span><img src="assets/error.svg"></div><div class="blocktext">                        <p class="blocktitle">Error prompt</p><p class="blockdesc">Triggers when a specified error happens</p>              </div></div></div>');
    flowy($("#canvas"), drag, release, snapping);
    
    function snapping(drag, first) {
            drag.children(".grabme").remove();
        drag.children(".blockin").remove();
        if (drag.children(".blockelemtype").val() == "1") {
            drag.append("<div class='blockyleft'><img src='assets/eyeblue.svg'><p class='blockyname'>New visitor</p></div><div class='blockyright'><img src='assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>When a <span>new visitor</span> goes to <span>Site 1</span></div>");
        } else if (drag.children(".blockelemtype").val() == "2") {
            drag.append("<div class='blockyleft'><img src='assets/actionblue.svg'><p class='blockyname'>Action is performed</p></div><div class='blockyright'><img src='assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>When <span>Action 1</span> is performed</div>");
        } else if (drag.children(".blockelemtype").val() == "3") {
            drag.append("<div class='blockyleft'><img src='assets/timeblue.svg'><p class='blockyname'>Time has passed</p></div><div class='blockyright'><img src='assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>When <span>10 seconds</span> have passed</div>");
        } else if (drag.children(".blockelemtype").val() == "4") {
            drag.append("<div class='blockyleft'><img src='assets/errorblue.svg'><p class='blockyname'>Error prompt</p></div><div class='blockyright'><img src='assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>When <span>Error 1</span> is triggered</div>");
        } else if (drag.children(".blockelemtype").val() == "5") {
            drag.append("<div class='blockyleft'><img src='assets/databaseorange.svg'><p class='blockyname'>New database entry</p></div><div class='blockyright'><img src='assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>Add <span>Data object</span> to <span>Database 1</span></div>");
        } else if (drag.children(".blockelemtype").val() == "6") {
            drag.append("<div class='blockyleft'><img src='assets/databaseorange.svg'><p class='blockyname'>Update database</p></div><div class='blockyright'><img src='assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>Update <span>Database 1</span></div>");
        } else if (drag.children(".blockelemtype").val() == "7") {
            drag.append("<div class='blockyleft'><img src='assets/actionorange.svg'><p class='blockyname'>Perform an action</p></div><div class='blockyright'><img src='assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>Perform <span>Action 1</span></div>");
        } else if (drag.children(".blockelemtype").val() == "8") {
            drag.append("<div class='blockyleft'><img src='assets/twitterorange.svg'><p class='blockyname'>Make a tweet</p></div><div class='blockyright'><img src='assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>Tweet <span>Query 1</span> with the account <span>@alyssaxuu</span></div>");
        } else if (drag.children(".blockelemtype").val() == "9") {
            drag.append("<div class='blockyleft'><img src='assets/logred.svg'><p class='blockyname'>Add new log entry</p></div><div class='blockyright'><img src='assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>Add new <span>success</span> log entry</div>");
        } else if (drag.children(".blockelemtype").val() == "10") {
            drag.append("<div class='blockyleft'><img src='assets/logred.svg'><p class='blockyname'>Update logs</p></div><div class='blockyright'><img src='assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>Edit <span>Log Entry 1</span></div>");
        } else if (drag.children(".blockelemtype").val() == "11") {
            drag.append("<div class='blockyleft'><img src='assets/errorred.svg'><p class='blockyname'>Prompt an error</p></div><div class='blockyright'><img src='assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>Trigger <span>Error 1</span></div>");
        }
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
        let components = entries[entryKey];

        html = '';
        for (let i in components) {
            html += generateBlockHtml(components[i].title, components[i].description, components[i].icon);
        }

        $("#blocklist").html(html);
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