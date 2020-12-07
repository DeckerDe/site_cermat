app.component('researchmodal', {
    props:{
      researcher_id:{
        type: Number,
        required: true,
      },
      researchers_list:{
        type: Array,
        required: true
      }
    },
    template:
    /*html*/ `
      <transition name="modal">
        <div class="modal-mask">
          <div class="modal-wrapper">
            <div class="modal-container">

              <div class="modal-header">
                <slot name="header">
                  <h2>{{researcher.name}}</h2>
                  <h4>Organização: {{researcher.organization}}</h4>
                  <h4>Sigla da Organização: {{researcher.organization_abre}}</h4>
                </slot>
              </div>

              <div class="modal-body">
                <slot name="body">
                  <div class="list_heading">
                    <h3> researchgate: </h3>
                    <span>{{researcher.researchgate}}</span>
                    <h3> Linkedin: </h3>
                    <span> {{researcher.linkedin}}</span>
                    <h3> Lattes: </h3>
                    <span> {{researcher.lattes}}</span>
                  </div>
                </slot>
              </div>
              <div class="modal-footer">
                <slot name="footer">
                  <button class="smallBtn" @click="$emit('close')">
                      OK
                  </button>
                </slot>
              </div>
            </div>
          </div>
        </div>
      </transition>`,
      data(){
          return{

          }
      },
      computed:{
        researcher(){
          function isResearcher(element, index, array){
            if(element.id === this.researcher_id){
              return true;
            }
            else return false;
          }

          var res = researchers_list.find(isResearcher, this)

          for(campo in res){
            if(res[campo] === "" ){
              res[campo] = "Não cadastrado."

            }
          }
          return res
        }
      }
})
