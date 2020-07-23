function pwshow() {
  var x = document.getElementById("pword");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

function dbancop(){
  let fname = document.getElementById("bancop").value;
  let url = "http://localhost:8000/static/data/";
  url = url.concat(fname);
  var windowFeatures = "menubar=yes,location=yes,resizable=yes,scrollbars=yes,status=yes";

  window.open(url, 'downloadBancop',windowFeatures);

}

function dConsol(){
  let fname = document.getElementById("Consolidado").value;
  let url = "http://localhost:8000/static/BrosCo_Si_Bancop_No/";
  url = url.concat(fname);
  var windowFeatures = "menubar=yes,location=yes,resizable=yes,scrollbars=yes,status=yes";

  window.open(url, 'downloadConsolidado',windowFeatures);

}
function dBrosCo(){
  let fname = document.getElementById("BrosCo").value;
  let url = "http://localhost:8000/static/BrosCo_Original/";
  url = url.concat(fname);
  var windowFeatures = "menubar=yes,location=yes,resizable=yes,scrollbars=yes,status=yes";

  window.open(url, 'downloadBrosCo',windowFeatures);

}
function dBog(){
  let fname = document.getElementById("Bancop_Original").value;
  let url = "http://localhost:8000/static/Bancop_Original/";
  url = url.concat(fname);
  var windowFeatures = "menubar=yes,location=yes,resizable=yes,scrollbars=yes,status=yes";

  window.open(url, 'downloadBancop_Original',windowFeatures);

}
