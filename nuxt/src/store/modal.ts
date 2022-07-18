const state = {
    isShowModal: false as boolean
}

const mutations = {
    openModal(state: any){
        state.isShowModal = true;
    },
    closeModal(state: any){
        state.isShowModal = false;
    }
}

const modal = {
    state,
    mutations,
}

export default modal
