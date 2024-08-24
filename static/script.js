$(document).ready(function() {
    $("#myButton").click(function() {
        $.get("/get_data", function(data) {
            $("#response").text(data.message);
        });
    });
});
