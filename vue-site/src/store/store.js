import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        viewStates: {
            loading: true,
            noContent: true,
            faq: false
        },
        detailedRowView: false,
        urank: "",
        urange: 1000,
        allMapData: [],
        filterMods: {
            HD: false,
            HR: false,
            DT: false,
            SD: false,
            PF: false,
            FL: false,
            EZ: false,
            NF: false,
            HT: false,
            SO: false
        },
        strict: false
    },
    mutations: {
        SET_VIEW_FAQ: (state, value) => state.viewStates.faq = value,
        SET_VIEW_LOADING: (state, value) => state.viewStates.loading = value,
        SET_VIEW_NOCONTENT: (state, value) => state.viewStates.noContent = value,
        SET_DETAILED_ROW_VIEW: (state, value) => state.detailedRowView = value,
        SET_URANK: (state, value) => state.urank = value,
        SET_URANGE: (state, value) => state.urange = value,
        SET_MAPDATA: (state, data) => state.allMapData = data,
        SET_MODS_TOGGLE(state, data) {
            console.log("Toggling Mod")
            state.filterMods[data] = !state.filterMods[data]
        },
        SET_STRICT_TOGGLE: (state, value) => state.strict = value
    },
    actions: {
        loadMapData({ commit }) {
            commit('SET_VIEW_LOADING', true);
            console.log(this.state.filterMods);
            var allMods = this.state.filterMods
            var mod_string = ""
            for (const mod of Object.keys(this.state.filterMods)) {
                if (allMods[mod]) {
                    mod_string += mod
                }
            }
            console.log(mod_string)

            axios
                .get('http://127.0.0.1:5001/api/get_top_maps',
                    {
                        params: {
                            urank: this.state.urank,
                            urange: this.state.urange,
                            mods: mod_string,
                            strict: this.state.strict
                        }
                    }
                )
                .then(r => r.data)
                .then(data => {
                    commit('SET_MAPDATA', data);
                    commit('SET_VIEW_LOADING', false)
                })
                .catch(function () {
                    console.log('error')
                    commit('SET_VIEW_LOADING', false)
                })
        },
        modToggleClick({ commit }, payload) {
            commit('SET_VIEW_LOADING', true)
            commit('SET_MODS_TOGGLE', payload)
        },
        strictToggleClick({ commit }) {
            commit('SET_VIEW_LOADING', true)
            commit('SET_STRICT_TOGGLE', !this.state.strict)
            console.log("Strict mode is now", this.state.strict)
        },
        contentIsShowing({ commit }, payload) {
            commit('SET_VIEW_NOCONTENT', payload)
        },
        contentIsLoading({ commit }, payload) {
            commit('SET_VIEW_LOADING', payload)
        },
        faqSectionToggle({ commit }) {
            commit('SET_VIEW_FAQ', !this.state.viewStates.faq)
            if (this.state.urank == "" && this.state.viewStates.faq == false) {
                commit('SET_VIEW_NOCONTENT', true)
            } else {
                commit('SET_VIEW_NOCONTENT', false)
            }
        },
        detailedRowViewToggle({ commit }) {
            commit('SET_DETAILED_ROW_VIEW', !this.state.detailedRowView)
            console.log("Detailed view is now", this.state.detailedRowView)
        }
    },
})
export default store;