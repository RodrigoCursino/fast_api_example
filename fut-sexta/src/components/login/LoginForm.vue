<template>
  <div class="login_form">
    <div class="form">
      <input  class="input_form"
              v-model="loginForm.cellphone" 
              type="tel"
      >
      <input  class="input_form"
              v-model="loginForm.password" 
              type="password"
      >
      <button class="input_form btn_login"
              @click="login()"
      >
        LOGAR
      </button>
      <button class="input_form btn_login"
              @click="teste()"
      >
        LOGAR
      </button>
    </div>
    <div class="footer">
      <img src="@/assets/img/background_login_form.jpg" />
    </div>
  </div>
</template>

<script>
import { UserMixin } from "@/modules/User/UserMixin.js"
import { AjaxMixin } from "@/mixins/AjaxMixin.js"
export default {
  name: "login-form",
  mixins: [
    AjaxMixin,
    UserMixin
  ],
  data: () => ({
    loginForm: {
      cellphone: "",
      password: ""
    }
  }),
  methods: {
    async login() {
        let data = await this.post('auth/login', this.loginForm)
        if(data?.status===200) {
          this.set_user(data.data)
          if(this.user) {
            this.$router.push({name: "home"})
          }
        }
    },
    async teste() {
        let data = await this.get('teams')
        if(data?.status===200) {
          console.info("teams ",data.data)
        }
    }
  }
}
</script>

<style lang="scss" scoped>
  $main_color: #090b15;
  .login_form {
    background-color: $main_color;
    height: 100vh;

    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 2fr 1fr;
    grid-template-areas: "content" "footer";

    .form {
      
      grid-area: content;
      
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      align-items: center;
      box-sizing: border-box;

      padding: 0em 3em;

      h3 {
        color: white;
        font-weight: bold;
        font-style: italic;
        font-size: 30px;
        margin-bottom: 1em;
      }
      
      .input_form {
        
        background-color: transparent;
        color: rgb(74, 219, 255);
        border: rgb(74, 219, 255) solid 1px;
        border-radius: 15px;
        
        margin-bottom: 1.2em;
        width: 100%;
        min-height: 50px;
        
        text-align: center;
        text-transform: uppercase;
        font-size: 1em;
        display: block;

        transition: box-shadow 1s;

        &.btn_login {
        
          background-color: rgb(12, 122, 150);
          color: #090b15;
          font-weight: bold;
          display: block;
          box-shadow:none;

          &:hover {
            background-color: rgb(15, 204, 252);
            outline: none;
            border-radius: 15px;
          }
        }

        &:focus {
          border: rgb(15, 204, 252) solid 1px;
          box-shadow: 0px 0px 8px rgb(74, 219, 255);
          outline: none;
          border-radius: 15px;
        }
      }
      
    }

    .footer {
      grid-area: footer;

      img {
        width: 100%;
        height: 100%;
        object-fit: fill;
      }
    }
  }
</style>