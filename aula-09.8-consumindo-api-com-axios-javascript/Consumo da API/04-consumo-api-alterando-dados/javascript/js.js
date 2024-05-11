// Capturando o botão de cadastrar
const createBtn = document.getElementById("createBtn")
// Escuta ao evento click no botão
createBtn.addEventListener("click", createGame)

// Capturando o botão de editar
const updateBtn = document.getElementById("updateBtn")
// Escuta ao evento click no botão
updateBtn.addEventListener("click", updateGame)

// Enviando uma requisição GET para API para listar todos os games
axios.get("http://localhost:5000/games").then((response) => {
    const games = response.data
    const listGames = document.getElementById("games")

    games.forEach((game) => {
      let item = document.createElement("li")

      // Setando os atributos ID, título, ano e descrição para cada game
      item.setAttribute("data-id", game._id)
      item.setAttribute("data-titulo", game.titulo)
      item.setAttribute("data-ano", game.ano)
      item.setAttribute("data-descricao", game.descricao)

      item.innerHTML = `<h4>${game.titulo}</h4>
        <p>Descrição: ${game.descricao}</p> 
        <p>Ano: ${game.ano}</p>
        <p>ID: ${game._id}</p>`

        var deleteBtn = document.createElement("button")
        deleteBtn.innerHTML = "Deletar"
        deleteBtn.classList.add("btn", "btn-danger", "mb-3")
        deleteBtn.addEventListener("click", () => {
          deleteGame(item)
        })

        var editBtn = document.createElement("button")
        editBtn.innerHTML = "Editar"
        editBtn.classList.add("btn", "btn-warning", "mb-3")
        editBtn.addEventListener("click", function(){
          loadForm(item)
        })

        item.appendChild(deleteBtn)
        item.appendChild(editBtn)
        listGames.appendChild(item)
      })
    }).catch((error) => {
      console.log(error)
    })

// Função para CADASTRAR games
function createGame() {

  const form = document.getElementById("createForm");
  form.addEventListener("submit", function(event) {
  event.preventDefault() // Evita o envio padrão do formulário
  })

  const tituloInput = document.getElementById("titulo")
  const descricaoInput = document.getElementById("descricao")
  const anoInput = document.getElementById("ano")

  const game = {
    titulo: tituloInput.value,
    descricao: descricaoInput.value,
    ano: anoInput.value,
  }
  axios.post("http://localhost:5000/games", game).then((response) => {
      if (response.status == 201) {
        alert("Game cadastrado!")
        location.reload()
      }
    }).catch((err) => {
      console.log(err)
    })
}

// Função para DELETAR games
function deleteGame(listItem) {
  const id = listItem.getAttribute("data-id")
  axios.delete(`http://localhost:5000/games/${id}`).then(response => {
      alert("Game deletado!")
      location.reload()
  }).catch(err => {
      console.log(err)
  })
}

// Função para carregar formulário de edição
function loadForm(listItem) {
  const id = listItem.getAttribute("data-id")
  const titulo = listItem.getAttribute("data-titulo")
  const descricao = listItem.getAttribute("data-descricao")
  const ano = listItem.getAttribute("data-ano")

  document.getElementById("idEdit").value = id
  document.getElementById("tituloEdit").value = titulo
  document.getElementById("descricaoEdit").value = descricao
  document.getElementById("anoEdit").value = ano

}

// Função para ALTERAR games
function updateGame() {
  const form = document.getElementById("editForm");
  form.addEventListener("submit", function(event) {
  event.preventDefault() // Evita o envio padrão do formulário
  })

  const idInput = document.getElementById("idEdit")
  const tituloInput = document.getElementById("tituloEdit")
  const anoInput = document.getElementById("anoEdit")
  const descricaoInput = document.getElementById("descricaoEdit")

  const game = {
    titulo: tituloInput.value,
    descricao: descricaoInput.value,
    ano: anoInput.value
  }

  var id = idInput.value

  axios.put(`http://localhost:5000/games/${id}`, game).then((response) => {
      if (response.status == 200) {
        alert("Game atualizado!")
        location.reload()
      }
    }).catch((err) => {
      console.log(err)
    })
}