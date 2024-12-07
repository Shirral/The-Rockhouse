const accessoriesLayer = $("#accessories-layer");
const accessories = $(".accessory-option");
const frames = $(".frame-option");

$("#accessory-options").on("change", ".accessory-option", function () {
    const accessoryImage = $(this).next().clone().appendTo("#accessories-layer"); // clone image & add to accessory div
    accessoryImage.css({
        position: "absolute",
        top: 0,
        left: 0,
        width: "100%",
        height: "auto",
        zIndex: 2,
    });

 
});

