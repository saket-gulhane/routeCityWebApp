const express = require("express");

const bodyParser = require("body-parser");

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));

app.use(bodyParser.json());

const spawn = require("child_process").spawn;

// const morgan = require("morgan");
// const fs = require("fs");

app.use(express.static(__dirname + "/public"));

app.get("/", function(req, res) {
  res.sendFile("./index.html", { root: __dirname + "/" });
  res.sendfile("/index.js", { root: __dirname + "/" });
  res.sendFile("graph.png", { root: __dirname + "/images" });
  res.sendFile("5.gif", { root: __dirname + "/images" });
});

app.post("/dataSent", timeout("60s"), function(req, res) {
  // console.log("json obj received");
  // console.log(req);

  console.log(req.body.cities);
  console.log(req.body.edges);
  //city list

  var cityList = req.body.cities;
  var edgeList = req.body.edges;
  console.log(cityList[0]);

  ///////////////////////////////////////////////////////////////////////////
  //python module
  try {
    const process = spawn("python", [
      "./pyhton/corePython.py",
      cityList,
      edgeList
    ]);

    process.stdout.on("data", data => {
      var op = data.toString();
      console.log(op);
      op = op.substring(1, op.length - 3);
      console.log(op);
      op = op.replace(/'/g, "");
      console.log(op);
      var fArr = op.split(",");
      console.log(fArr);

      var final = JSON.stringify({ status: "ok", output: fArr });
      console.log(final);
      res.send(final);
    });
  } catch (err) {
    console.log(err);
  }
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`running on port--${port}`);
});
