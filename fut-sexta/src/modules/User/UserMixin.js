
import { mapState, mapActions, mapGetters } from 'vuex';

export const UserMixin = {
  computed: {
    ...mapState('User',{
                   user: state => {
                       return state.user;
                   }
               }
    )
  },
  methods: {
    ...mapActions('User',['set_user']),
    ...mapGetters('User',['get_token']),
  }
}