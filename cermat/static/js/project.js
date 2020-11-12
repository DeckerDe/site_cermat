/* Project specific Javascript goes here. */

const app = Vue.createApp({
    data(){
        return{
            showNav: false,
            teste: "Tenho acesso",
            showModal: false,
            researcherId: 0,

        }
    },
    methods:{
        toggleMenu(){
            if(this.showNav){
                this.showNav = false;
            }
            else this.showNav = true;
        },
        researcherModal(researcher_id){
            this.showModal = true;
            this.researcherId = researcher_id;
            console.log(researcher_id)
        }
    },
    delimiters: ['[[', ']]'],
})
