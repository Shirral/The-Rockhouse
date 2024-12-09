const accessoriesLayer = $("#accessories-layer");
const accessories = $(".accessory-option");
const frames = $(".frame-option");

$("#accessory-options").on("change", ".accessory-option", function () {
    let accessoryId = $(this).val();
    
    let accessoryImage = $(this).next().clone().attr("data-accessory-id", accessoryId) // clone image & add to accessory div & copy its id from value

    if (this.checked) {
        accessoryImage.css({
            position: "absolute",
            top: 0,
            left: 0,
            width: "100%",
            height: "auto",
            zIndex: 2,
        });

        accessoryImage.appendTo("#accessories-layer");
    } else {
        
        $(`#accessories-layer [data-accessory-id="${accessoryId}"]`).remove();
    }

});

$("#frame-options").on("change", ".frame-option", function () {
    let frameId = $(this).val();

    $("#frames-layer").empty();

    // if the -no frame- option is selected, end here - do not add anything else
    if (frameId == "frame_none"){
        return;
    }

    let frameImage = $(this).next().clone().attr("data-frame-id", frameId) // clone image & add to accessory div & copy its id from value
    frameImage.css({
        position: "absolute",
        top: 0,
        left: 0,
        width: "100%",
        height: "auto",
        zIndex: 3,
    });
    
    frameImage.appendTo("#frames-layer");

});
