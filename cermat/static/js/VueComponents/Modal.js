app.component('modal', {
    template:
    /*html*/ `
      <transition name="modal">
        <div class="modal-mask">
          <div class="modal-wrapper">
            <div class="modal-container">

              <div class="modal-header">
                <slot name="header">
                  default header
                </slot>
              </div>

              <div class="modal-body">
                <slot name="body">
                  default body
                </slot>
              </div>

              <div class="modal-footer">
                <slot name="footer">
                  default footer
                </slot>
                <button class="modal-default-button" @click="$emit('close')">
                    OK
                </button>
              </div>
            </div>
          </div>
        </div>
      </transition>`,
      data(){
          return{

          }
      }
})
