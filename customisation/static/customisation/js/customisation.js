const accessoriesLayer = $("#accessories-layer");
const accessories = $(".accessory-option");
const frames = $(".frame-option");

// listen for changes on accessory checkboxes
$("#accessory-options").on("change", ".accessory-option", function () {
    let accessoryId = $(this).val();
    
    // clone image, add it to the accessory div & copy its id from value
    let accessoryImage = $(this).next().clone().attr("data-accessory-id", accessoryId);

    // styling of the newly created image element
    if (this.checked) {
        accessoryImage.css({
            position: "absolute",
            top: "3.75%",
            left: "3.5%",
            width: "93%",
            height: "auto",
            zIndex: 2,
            borderRadius: "20px"
        });

        // show the newly created image element as a layer in the
        // #accessories-layer div
        accessoryImage.appendTo("#accessories-layer");
    } else {
        // remove the un-checked image element from the
        // #accessories-layer div
        $(`#accessories-layer [data-accessory-id="${accessoryId}"]`).remove();
    }

});

// add the same functionality as above to the dframes and their radio buttons
$("#frame-options").on("change", ".frame-option", function () {
    let frameId = $(this).val();

    // empty the frame layer - selection of another frame automatically deselects other frames
    // as only one frame can be selected at the time
    $("#frames-layer").empty();

    // if the -no frame- option is selected, end here - do not add anything else
    if (frameId == "frame_none"){
        return;
    }

    let frameImage = $(this).next().clone().attr("data-frame-id", frameId); // clone image & add to accessory div & copy its id from value
    frameImage.css({
        position: "absolute",
        top: "3.75%",
        left: "3.5%",
        width: "93%",
        height: "auto",
        zIndex: 3,
        borderRadius: "20px"
    });
    
    // show the newly created image element as a layer in the
    // #frames-layer div
    frameImage.appendTo("#frames-layer");

});
