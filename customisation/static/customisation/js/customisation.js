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
        // accessoryImage.remove();
    }

});

