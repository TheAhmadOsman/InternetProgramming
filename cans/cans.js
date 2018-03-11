class Can {
    constructor(height, radius) {
        this._height = height
        this.radius = radius
    }

    //volume() for a method
    //get for a simple property
    get volume() {
        return this.radius * this.radius * Math.PI * this._height
    }

    set volume(nv) {
        console.log("Error: You cannot change the volume!")
    }

    get height() {
        return this._height
    }

    set height(nv) {
        if (nv <= 0) {
            console.log("Cans cannot have a negative or zero height!")
        } else {
            this._height = nv
        }
    }
}

coke = new Can(10, 1)
console.log(coke.volume)
coke.volume = 15

console.log(coke.height)
coke.height = 22
console.log(coke.height)
coke.height = -5
console.log(coke.height)