// MODEL
const model = {
  catSprites: [
    'images/cat01.svg',
    'images/cat02.svg',
    'images/cat03.svg',
    'images/cat04.svg',
    'images/cat05.svg',
    'images/cat06.svg',
    'images/cat07.svg',
    'images/cat08.svg',
    'images/cat09.svg',
    'images/cat10.svg',
    'images/cat11.svg',
    'images/cat12.svg',
  ],
  catNames: ['Misha', 'Chibi'],
}

// VIEW
const view = {
  init: () => {
    for (let i of octopus.allCats) {
      // create cat list
      const catList = document.querySelector('ul')
      const catInList = document.createElement('li')
      catList.appendChild(catInList)
      const catImage = document.createElement('img')
      catImage.setAttribute('src', i.mishaImage)
      catInList.appendChild(catImage)
      const catName = document.createElement('h3')
      catName.innerHTML = i.mishaName
      catInList.appendChild(catName)

      // select the cat from list
      catImage.addEventListener('click', () => {
        const catElem = document.querySelector('.cat')
        catElem.innerHTML = ''
        const catPic = document.createElement('img')
        catPic.setAttribute('src', i.mishaImage)
        catElem.appendChild(catPic)
        const meowElement = document.createElement('h2')
        meowElement.innerHTML = `${i.mishaName} meow count: ${i.meowCount}`
        catElem.appendChild(meowElement)
        const catNames = [...document.querySelectorAll('.selected')]
        catNames.map((item) => item && item.classList.remove('selected'))
        catName.classList.add('selected')

        // cat clicker
        catPic.addEventListener('click', () => {
          i.meowCount++
          catPic.setAttribute('src', i.randImage())
          i.mishaImage = catPic.src
          meowElement.innerHTML = `${i.mishaName} meow count: ${i.meowCount}`
          catName.innerHTML = `${i.mishaName} (${i.meowCount})`
        })
      })
    }
  },
}

// OCTOPUS
class Misha {
  constructor() {
    this.meowCount = 0
    this.mishaImage = this.randImage()
    this.mishaName = ''
  }
  randImage() {
    const mishaSprite =
      model.catSprites[Math.floor(Math.random() * model.catSprites.length)]
    return mishaSprite
  }
}
// create cat instances
const octopus = {
  allCats: [],
  init: (num) => {
    for (let i = 0; i < num; i++) {
      let cat = new Misha()
      octopus.allCats.push(cat)
      octopus.allCats[i].mishaName = model.catNames[i] || 'Abandoned Pet'
    }
    view.init()
  },
}

octopus.init(3)
