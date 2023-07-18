<template>
<!--
  <v-card class="fill-height" flat>
    <v-toolbar
      color="primary"
      dark
      extended
      flat
    >
    </v-toolbar>
    <v-layout row justify-center pb-2 style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;" row wrap>
      <v-flex xs11 sm10 md8>
        <v-card class="card--flex-toolbar" >
          <v-card>
            <v-container grid-list-lg fluid>
              <h2 class="headline primary--text mb-3" style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">Mentors</h2>
              <p class="font-italic">You can also pitch your own project idea to these mentors. Feel free to contact any
                mentor via email/phone and talk to them about the project idea, ask the mentor to float the project if
                she/he agrees to mentor you with your proposed project. A mentor has to create the project for it to be
                considered a valid project.</p>
              <v-layout row wrap align-center justify-center>
                <v-flex
                  v-for="(mentor, i) in mentorList"
                  :key="i"
                  sm12 md6 lg5 
                  
                >
                <v-spacer></v-spacer>
                  <v-card class="elevation-5 my-4 rounded-card" :class="{ 'card-hover': isCardHovered === i }" @mouseover="isCardHovered = i" @mouseleave="isCardHovered = null" >
                    <v-card-text>
                      <v-layout row column align-center justify-center>
                        <v-avatar size="128">
                          <GAvatar :email="mentor.email" :size="128"/>
                        </v-avatar>
                        <div class="headline">{{mentor.first_name + ' ' + mentor.last_name}}</div>
                        <v-list>
                          <v-list-tile>
                            <v-list-tile-action>
                              <v-icon>fa-envelope</v-icon>
                            </v-list-tile-action>
                            <v-list-tile-content><a :href="`mailto:${mentor.email}`">{{ mentor.email }}</a>
                            </v-list-tile-content>
                          </v-list-tile>
                          <v-list-tile>
                            <v-list-tile-action>
                              <v-icon>fa-phone</v-icon>
                            </v-list-tile-action>
                            <v-list-tile-content><a :href="`mailto:${mentor.phone}`">{{ mentor.phone }}</a>
                            </v-list-tile-content>
                          </v-list-tile>
                        </v-list>
                        <v-flex><p>{{mentor.about_me}}</p></v-flex>
                      </v-layout>
                    </v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card>
        </v-card>
      </v-flex>
    </v-layout>
  </v-card>
-->



 <v-card class="fill-height" flat>
    <v-toolbar color="primary" dark extended flat></v-toolbar>
    <v-layout row justify-center pb-2 style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">
      <v-flex xs12 sm10 md8>
        <v-card class="card--flex-toolbar">
          <v-container grid-list-lg fluid>
            <h2 class="headline primary--text mb-3" style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">Mentors</h2>
            <p class="font-italic">You can also pitch your own project idea to these mentors. Feel free to contact any mentor via email/phone and talk to them about the project idea, ask the mentor to float the project if she/he agrees to mentor you with your proposed project. A mentor has to create the project for it to be considered a valid project.</p>
            <v-row justify="center" class="mb-4">
              <v-col cols="12" sm="6" md="4" lg="3" v-for="(mentor, i) in mentorList" :key="i">
                <v-card class="elevation-9 my-4 rounded-card" :class="{ 'card-hover': isCardHovered === i }" @mouseover="isCardHovered = i" @mouseleave="isCardHovered = null">
                  <v-card-text>
                    <div class="mentor-info">
                      <div class="name-wrapper">
                        <div class="headline">{{ mentor.first_name + ' ' + mentor.last_name }}</div>
                        <v-list>
                          <v-list-item>
                         
                            <v-list-item-action>
                             <a :href="`mailto:${mentor.email}`" target="_blank">
                              <v-icon class="github-icon">fa-envelope</v-icon>
                            </a>
                            </v-list-item-action>

                            </v-list-item>


               
                          <v-list-item>
                            <v-list-item-action>
                            <a :href="`https://wa.me/${mentor.phone}`" target="_blank">
                              <v-icon class="github-icon">fa-whatsapp</v-icon>
                              </a>
                            </v-list-item-action>

              

                            <v-list-item-action>
                            <a :href="mentor.github" target="_blank">
                              <v-icon class="github-icon">fa-github</v-icon>
                              </a>
                            </v-list-item-action>


                             
                    
                          </v-list-item>
                        </v-list>
                      </div>
                        <div class="space"></div>

                      <v-avatar size="128" class="custom-margin-left" align="center">
                        <GAvatar :email="mentor.email" :size="128"/>
                      </v-avatar>
                      <v-spacer></v-spacer>

                      
                    </div>
                    <v-spacer></v-spacer>
                     
                    <p class="about-me">{{ mentor.about_me }}</p>
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-flex>
    </v-layout>
  </v-card>
</template>




<script>
  import GAvatar from './GAvatar'
  import {mapGetters, mapActions} from 'vuex'

  export default {
    name: 'MentorList',
    components: {GAvatar},
    computed: {
      ...mapGetters('mentorList', ['mentorList'])
    },
    methods: {
      ...mapActions('mentorList', ['fetchMentorList'])
    },
     data() {
      return {
        isCardHovered: null
      };
    },
    mounted () {
      if (!this.mentorList.length) this.fetchMentorList()
    }
  }
</script>

<style scoped>
  .card--flex-toolbar {
    margin-top: -64px;
  }

  .v-list__tile__content > a {
    text-decoration: none;
  }


.mentor-info {
  display: flex;
  align-items: center;
}

.name-wrapper {
  text-align: center;
  margin-right: 16px;
}

.about-me {
  margin-top: 15px;
  text-align: center;
}

.headline {
  margin-bottom: 8px;
  margin-left: 16px;
}


  .rounded-card {
  border-radius: 10px;
  border: 1px solid linear-gradient(to right, #0088FF, #00BFFF, #00E5FF);
  
}
 
 .custom-margin-left {
  display: flex;
  justify-content: flex-end;
}
  
  .card-hover {
  border-radius: 10px;
  transform: translateY(0);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s, box-shadow 0.3s;
  
}

.card-hover:hover {
  border-radius: 20px;
 transform: translateY(-8px); 
  box-shadow: 0px 0px 30px 1px rgba(0, 255, 117, 0.30);
  transform: scale(1.04);
  
}


.space {
  flex-grow: 5;
}


  

  .v-list {
    list-style-type: none;
    padding: 10px;}

  
.github-icon{
  color: #000000; 
  margin: 5px;
}

.github-icon:hover{
  color: #357351

}

</style>
