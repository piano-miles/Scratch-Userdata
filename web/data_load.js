let zipResponse = await fetch("./data.zip");
let zipBinary = await zipResponse.arrayBuffer();
pyodide.unpackArchive(zipBinary, "zip");