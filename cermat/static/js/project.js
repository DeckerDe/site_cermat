/* Project specific Javascript goes here. */

const app = Vue.createApp({
    data(){
        return{
            showNav: false,
            teste: "Tenho acesso",
            showModal: false,
            researcher_id: 0,
            researchers_list: [],

        }
    },
    computed:{
        isBigEnough(){
            return window.innerWidth > 760;
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
            this.researcher_id = researcher_id;
            this.researchers_list = researchers_list
            //console.log(researcher_id)
        }
    },
    delimiters: ['[[', ']]'],
})
