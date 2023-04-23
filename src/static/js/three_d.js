var night_ctnr = document.querySelector('#night_ctnr')
if (night_ctnr){
    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth/window.innerHeight,
        0.1,
        1000
        )
    camera.position.z = 30


    var renderer = new THREE.WebGLRenderer({
        antialias: true
    })

    renderer.setClearColor(new THREE.Color('#111'))

    renderer.setSize(window.innerWidth, window.innerHeight)

    night_ctnr.appendChild(renderer.domElement)


    const hemi_light = new THREE.HemisphereLight( 0xFFFFFF, 10 );
    scene.add(hemi_light)


    const point_light = new THREE.PointLight(0xFFFFFF, 1, 2)
    point_light.position.set(-2, 7, -10);
    // scene.add(point_light)

    //star system
    const particles_geomtery = new THREE.BufferGeometry;
    const particles_count = 10000/2;

    const position_array = new Float32Array(particles_count * 3)

    for (let i = 0; i < particles_count * 3; i++){
        position_array[i] = (Math.random() - 0.5) * 70
    }

    particles_geomtery.setAttribute('position', new THREE.BufferAttribute(position_array, 3))

    const particle_material = new THREE.PointsMaterial({
        // size: 0.010,
        size: 0.005,
        color: 'white',
    })
    const particles_mesh = new THREE.Points(particles_geomtery, particle_material)
    scene.add(particles_mesh)

    function load_moon(){
        const moon_link = night_ctnr.dataset.moon_model
        const moon_loader = new THREE.GLTFLoader();
        moon_loader.load(
            moon_link,
            function ( gltf ) {
                moon = gltf.scene;
                moon.position.set(1, 5, 8)
                scene.add( moon );
            },
        )
    }

    function load_planet(){
        const planet_link = night_ctnr.dataset.planet_model
        const planet_loader = new THREE.GLTFLoader();    
        planet_loader.load(
            planet_link,
            function ( gltf ) {
                planet = gltf.scene;
                planet.scale.set(8, 8, 8)
                planet.position.set(4, 18, -20)
                scene.add( planet );
            },
        )
    }

    function load_ship(){
        const ship_link = night_ctnr.dataset.ship_model
        const ship_loader = new THREE.GLTFLoader();
        ship_loader.load(
            ship_link,
            function ( gltf ) {
                ship = gltf.scene;
                ship.scale.set(.5, .5, .5)
                ship.position.set(4, 4, 15)
                scene.add( ship );
            },
        )
    }


    let mouse_x = 0
    let mouse_y = 0

    function animateParticles(event){
        mouse_y = event.clientY
        mouse_x = event.clientX
    }

    document.addEventListener('mousemove', animateParticles)

    window.addEventListener('resize', ()=> {
        renderer.setSize(window.innerWidth, window.innerHeight);
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix()
    })

    const clock = new THREE.Clock()
    var loaded_components = false
    var render = function (){
        requestAnimationFrame(render)

        let elasped_time = clock.getElapsedTime()
        

        try {
            if (moon){
                moon.rotation.y += 0.003;

            }

            if (planet){
                planet.rotation.y += 0.002;
                planet.rotation.x += 0.001;
            }


            if (ship){
                ship.rotation.y -= 0.003;
                ship.rotation.x += 0.003;

            }

            if (elasped_time > 15 && elasped_time < 20){
                ship.position.y += .001
                ship.position.x -= .01
                clock.stop()
            } else {
                ship.position.y -= .001
                ship.position.x += .01
                ship.position.z += .01
            }


            if (window.innerWidth > 1399){
                moon.position.set = (-5, 0, 6)
                point_light.position.z = 16
                planet.position.set(12, 30, -25)
            } else {
                moon.position.set = (1, 5, 8)
                point_light.position.z = 8
            }

        } catch (error) {
            // console.log('3d assets are still loading')
        }


        particles_mesh.rotation.y = (.005 * elasped_time)
        particles_mesh.rotation.x = (.0009 * -mouse_y)
        particles_mesh.rotation.x = (.0009 * -mouse_x)
        particles_mesh.rotation.z = (.0009 * -mouse_y)
        particles_mesh.rotation.z = (.0009 * -mouse_x)

        if (! loaded_components){
            if (elasped_time > 2 && elasped_time < 3){ 
                load_moon()
                if (window.innerWidth > 1400){
                    load_planet()
                    load_ship()

                }
                loaded_components = true
            }
        }

        renderer.domElement.id = 'globe_canvas';
        renderer.render(scene, camera)

    }
    render();
}

// this section handles controls and manipulation of the camera
var index_hero_ctnr = document.querySelector('.hero_ctnr')
var hero_text = document.querySelector('.text_ctnr')
var control_panel = document.querySelector('.controls_ctnr')
var mountain = document.querySelector('#mountain')
var control_sets = document.querySelectorAll('.control_set')
var control_message = document.querySelector('#controls_ctnr_message')
var control_buttons = document.querySelectorAll('.control_button')

const show_controls_tl = gsap.timeline({
    paused: true,  
})

// mountain.style.transition = "2s"
// mountain.style.opacity = 0

show_controls_tl.to(
    mountain,
    {
        opacity: 0,
        duration: .15,
        ease: Sine.easeInOut,
        display: 'none',
    },
    1
), 1

show_controls_tl.to(
    hero_text,
    {
        opacity: 0,
        duration: .15,
        ease: Sine.easeInOut,
        display: 'none',
    },
    1
), 1

show_controls_tl.to(
    control_panel,
    {
        duration: 1,
        left: '2em',
        x: '-20em',    
        ease: Sine.easeInOut,
    }
), 1



function handleKeyDown(event, custom_action=false){
    if (custom_action){
        var action = custom_action
    } else {
        var action = event.key.toLowerCase()
    }
    

    element = document.querySelector(`#${action}`)
    console.log(element)

    element.classList.add('apply_click_light')

    // element.style.transition = '.5s'
    // element.style.filter = 'brightness(2)'
    // element.style.filter = 'none'



    if (action==='w'){
        camera.position.z -= 1
    }

    if (action==='s'){
        camera.position.z += 1
    }

    if (action==='d'){
        camera.position.x += 1
    }
    if (action==='a'){
        camera.position.x -= 1
    }

    if (action==='q'){
        camera.position.y += 1
    }
    if (action==='e'){
        camera.position.y -= 1
    }

    setTimeout(function(){
        element.classList.remove('apply_click_light')
    }, 250)

}

function handleKeyUp(event){
    let action = event.key.toLowerCase()

    if (action==='enter'){
        control_message.innerText = 'controls for the camera'
    
        show_controls_tl.play()

  
        for (let elem of control_sets){
            elem.style.display = 'flex';
        }

        for (let elem of control_buttons){
            elem.addEventListener('click', handleControlClick, false)
        }


        document.addEventListener('keydown', handleKeyDown)
        document.removeEventListener('keyup', handleKeyUp)
    }
}

document.addEventListener('keyup', handleKeyUp)


function handleControlClick(event){
    handleKeyDown(event, custom_action=event.target.id)
}