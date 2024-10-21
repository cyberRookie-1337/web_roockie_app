from flask import Flask , jsonify
import random
app = Flask(__name__)


space_facts = [
    "Space is completely silent because there is no atmosphere.",
    "Neutron stars can spin 600 times per second.",
    "A day on Venus is longer than a year on Venus.",
    "There are more stars in the universe than grains of sand on Earth.",
    "The footprints on the Moon will stay there for millions of years.",
    "One million Earths could fit inside the sun.",
    "The hottest planet in our solar system is Venus.",
    "The coldest place in the universe is the Boomerang Nebula.",
    "A spoonful of a neutron star would weigh about 6 billion tons.",
    "There are more than 100 billion galaxies in the observable universe.",
    "The universe is approximately 13.8 billion years old.",
    "Saturn's rings are made mostly of ice particles.",
    "If two pieces of the same type of metal touch in space, they will bond permanently.",
    "The Great Wall of Galaxies is the largest known structure in the universe.",
    "Jupiter has the most moons of any planet in our solar system.",
    "Light from the Sun takes about 8 minutes to reach Earth.",
    "Mercury is the closest planet to the Sun.",
    "The largest volcano in the solar system is Olympus Mons on Mars.",
    "There are estimated to be 200 billion stars in our Milky Way galaxy.",
    "The Andromeda Galaxy is on a collision course with the Milky Way.",
    "The Voyager 1 spacecraft is the farthest human-made object from Earth.",
    "Black holes are regions in space where gravity is so strong that nothing can escape.",
    "The largest known star is UY Scuti.",
    "Earth is the only known planet to support life.",
    "Astronauts can grow up to 2 inches taller in space due to the lack of gravity.",
    "The Moon is drifting away from Earth at a rate of about 1.5 inches per year.",
    "There are no seasons on Jupiter due to its axial tilt of only 3 degrees.",
    "The Milky Way galaxy is on a collision course with the Andromeda galaxy.",
    "Space is not completely empty; it has low-density particles and radiation.",
    "The ISS travels at a speed of 17,500 miles per hour.",
    "Pluto was reclassified from a planet to a dwarf planet in 2006.",
    "The largest known galaxy is IC 1101.",
    "There are floating water reservoirs in space, containing 140 trillion times the water in Earth's oceans.",
    "The speed of light is approximately 299,792 kilometers per second.",
    "Saturn could float in water because it is mostly made of gas.",
    "The first living creature in space was a dog named Laika.",
    "Mars has the largest dust storms in the solar system.",
    "A day on Mars is just over 24 hours long.",
    "The closest star to Earth, Proxima Centauri, is 4.24 light-years away.",
    "The observable universe is about 93 billion light-years in diameter.",
    "Asteroids are remnants from the formation of the solar system.",
    "A year on Mercury is just 88 Earth days.",
    "The temperature on the surface of the Sun is about 5,500 degrees Celsius.",
    "The Sun makes up about 99.86% of the mass of the entire solar system.",
    "Galaxies can collide, and the Milky Way has collided with others in the past.",
    "The first person to walk on the Moon was Neil Armstrong in 1969.",
    "A quasar is a highly luminous and active galactic nucleus.",
    "The universe is continuously expanding.",
    "Earth is the only planet not named after a god.",
    "The largest known structure in the universe is the Hercules-Corona Borealis Great Wall.",
    "The concept of time travel is a common theme in science fiction."
]

@app.route('/')
def random_fact():
    fact = random.choice(space_facts)
    return jsonify({'random fact about space': fact})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=34678)
