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
                  <h3>{{researcher.name}}</h3>
                </slot>
              </div>

              <div class="modal-body">
                <slot name="body">
                  <p> {{researcher.researchgate}} </p>
                </slot>
              </div>
              <div class="modal-footer">
                <slot name="footer">
                  default footer
                </slot>
              </div>
              <button class="modal-default-button" @click="$emit('close')">
                    OK
                </button>
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


          return res
        }
      }
})
