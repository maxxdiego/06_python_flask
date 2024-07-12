// Capturando o botão de cadastrar
const createBtn = document.getElementById("createBtn")
// Escuta ao evento click no botão
createBtn.addEventListener("click", createGame)

// Enviando uma requisição GET para API para listar todos os games
axios.get("http://localhost:5000/games").then((response) => {
    const games = response.data
    const listGames = document.getElementById("games")

    games.forEach((game) => {
      let item = document.createElement("li")

      // Setando o atributo ID para cada game
      item.setAttribute("data-id", game._id)

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