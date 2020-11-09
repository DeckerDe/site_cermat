/* Project specific Javascript goes here. */
const app = Vue.createApp({
    data(){
        return{
            showNav: false,
            teste: "Tenho acesso",
            projects: null,
            showModal: false,
        }
    },
    methods:{
        toggleMenu(){
            if(this.showNav){
                this.showNav = false;
            }
            else this.showNav = true;
        },
    },
    delimiters: ['[[', ']]'],
})
