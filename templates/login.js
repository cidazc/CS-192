let app = new Vue({
  el: '#app',
  data: {
    frameworks: [
      { name: 'Aso', votes: 0 },
      { name: 'Dog', votes: 0 },
      { name: 'Awu', votes: 0 }
    ]
  },
  methods: {
    voteFor: function(f) {
      f.votes += 1
    },
    addNew: function(event) {
      this.frameworks.push({
        name: event.target.value,
        votes: 0
      })
      event.target.value = ''
    },
    remove: function(f) {
      this.frameworks = this.frameworks.filter(i => i != f)
    }
  }
})

let accounts = new Vue({
  el: '#accounts',
  data: {
    frameworks: [
      { name: 'Allan' },
      { name: 'Cid'},
      { name: 'Reyster'}
    ]
  },
  methods: {
    addNew: function(event) {
      this.frameworks.push({
        name: event.target.value,
      })
      event.target.value = ''
    },
    remove: function(f) {
      this.frameworks = this.frameworks.filter(i => i != f)
    }
  }
})
