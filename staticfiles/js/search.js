 
 function cargarJSON(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.overrideMimeType("application/json");
    xhr.open('GET', url, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            callback(xhr.responseText);
        }
    };
    xhr.send(null);
}

// Función para buscar por ID
function buscarPorID() {
    var idInput = document.getElementById('idInput').value;
    var tableContainer = document.getElementById('tableContainer');
    var tableHTML = '';

    // Limpiar la tabla antes de agregar nuevos elementos
    tableContainer.innerHTML = '';

    // Cargar el JSON desde un archivo independiente
    cargarJSON("../static/json/tarjetones.json", function(response) {
        var data = JSON.parse(response);

        // Buscar el ID en el JSON
        data.tarjetones.forEach(function(tarjeton) {
            if (tarjeton.id == idInput) {
                // Construir la tabla con los elementos encontrados
                tableHTML += '<table class="table">';
                tableHTML += '<thead><tr><th>Letra</th><th>Números</th></tr></thead>';
                tableHTML += '<tbody>';
                for (var letra in tarjeton) {
                    if (letra !== 'id') {
                        tableHTML += '<tr>';
                        tableHTML += '<td>' + letra + '</td>';
                        tableHTML += '<td>' + tarjeton[letra].join(', ') + '</td>';
                        tableHTML += '</tr>';
                    }
                }
                tableHTML += '</tbody></table>';
            }
        });

        // Insertar la tabla en el contenedor
        tableContainer.innerHTML = tableHTML;
    });
}