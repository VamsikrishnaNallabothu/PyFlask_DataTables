$(document).ready(function() {
    var myData = [
        {"name" : "n1", "surname" : "g", "age" : "75"},
        {"name" : "n2", "surname" : "g", "age" : "90"},
        {"name" : "n3",  "surname" : 'n', "age" : "23"},
        {"name" : "n4",  "surname" : 'n', "age" : "24"},
        {"name" : "n5",  "surname" : 'n', "age" : "48"},
        {"name" : "n6",  "surname" : "n", "age" : "49"},
    ];

    $("#myTable").DataTable({
        "data" : myData,
        "columns" : [
        {"render" : function() {
            return '<input type = "checkbox">';
        }},
        {"data" : "name"},
        {"data" : "surname"},
        {"data" : "age"}
        ]
    });

});