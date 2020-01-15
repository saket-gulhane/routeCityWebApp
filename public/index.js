function operation() {
  var content = document.getElementById("input1").value;

  if (content.length < 1) {
    window.alert("Enter cities name please!!!");
  } else {
    $("#loadingmessage").show();
    $("#buttonSent").attr("disabled", true);

    //take city list
    var jsonCities = $("#input1")
      .val()
      .split("\n");
    // var jsonCities = JSON.stringify(cities);
    console.log(jsonCities);

    //take edges list
    var edgeCount = document.getElementById("input2").value;
    if (edgeCount.length < 1) {
      var jsonEdges = "a-aa";
    } else {
      var jsonEdges = $("#input2")
        .val()
        .split("\n");
    }
    // var jsonEdges = JSON.stringify(edges);
    console.log(jsonEdges);

    // var sentJson = {
    //   cities: jsonCities,
    //   edges: jsonEdges
    // };

    var p1 = { cities: jsonCities, edges: jsonEdges };
    var jsonf = JSON.stringify(p1);

    $.ajax({
      url: "/dataSent",
      type: "POST",
      contentType: "application/json",
      data: jsonf,
      success: function(res) {
        $("#loadingmessage").hide();
        document.getElementById("scroll").innerHTML =
          "Scroll down for the route...";

        // success callback
        var outJson = JSON.parse(res);
        var count = outJson.output[0];
        var array = outJson.output;
        console.log(array);

        fillTable(array, count);
        console.log(array[array.length - 1]);
        document.getElementById("distance").innerHTML =
          "Total length of path: " +
          parseInt(array[array.length - 1], 10) +
          " km";

        $("#buttonSent").attr("disabled", false);
      }
    });
  }
}

function fillTable(arr, count) {
  const tableBody = document.getElementById("tableData");
  let dataHTML = "";

  for (var i = 0; i < count; i++) {
    console.log(arr[i + 1]);
    var list = arr[i + 1].split(" ");
    dataHTML +=
      "<tr><td>" +
      list[1] +
      "</td><td>" +
      list[2] +
      "</td><td>" +
      parseInt(list[3], 10) +
      " km" +
      "</td></tr>";
  }
  console.log(dataHTML);
  tableBody.innerHTML = dataHTML;
}
