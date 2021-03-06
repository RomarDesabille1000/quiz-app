"use strict";(self.webpackChunkreact_webpack_setup=self.webpackChunkreact_webpack_setup||[]).push([[738],{738:(e,t,a)=>{a.r(t),a.d(t,{default:()=>p});var n=a(8152),l=a(5861),r=a(7757),s=a.n(r),o=a(7294),m=a(6550),c=a(8767),i=a(9189);const u=function(e){var t=e.title,a=e.text;return o.createElement("div",{className:"z-50 overflow-hidden opacity-75 flex flex-col items-center justify-center"},o.createElement("div",{className:"loader ease-linear rounded-full border-4 border-t-4 border-gray-200 h-12 w-12 mb-4"}),o.createElement("h2",{className:"text-center text-gray-900 text-xl font-semibold"},t||"Loading..."),o.createElement("p",{className:"w-1/3 text-center text-gray-900"},a||"This may take a few seconds, please dont close this page. "))};var d=a(8220);const p=function(){var e,t=(0,m.UO)().slug,a=(0,c.useQueryClient)(),r=(0,c.useQuery)(["quizContent",t],(function(){return i.Z.getQuizContent(t)}),{enabled:void 0!==t}),p=r.data,x=r.isLoading,f=(0,c.useMutation)(i.Z.submitQuiz,{onSettled:(e=(0,l.Z)(s().mark((function e(){return s().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,a.invalidateQueries("quizContent");case 2:case"end":return e.stop()}}),e)}))),function(){return e.apply(this,arguments)})}),v=f.mutate,N=f.isLoading,g=(0,o.useState)("00"),E=(0,n.Z)(g,2),b=E[0],w=E[1],h=(0,o.useState)("00"),y=(0,n.Z)(h,2),k=y[0],q=y[1],z=(0,o.useState)("00"),S=(0,n.Z)(z,2),_=S[0],Z=S[1],C=(0,o.useState)("00"),M=(0,n.Z)(C,2),D=M[0],Q=M[1],I=(0,o.useRef)();(0,o.useEffect)((function(){if(null==p||!p.submitted){var e=new Date((0,d.p6)(null==p?void 0:p.quiz_end)).getTime(),t=setInterval((function(){var t=new Date((0,d.x7)()).getTime(),a=e-t,n=Math.floor(a/864e5),l=Math.floor(a%864e5/36e5),r=Math.floor(a%36e5/6e4),s=Math.floor(a%6e4/1e3);a<0?I.current.click():(w(n<10?"0".concat(n):n),q(l<10?"0".concat(l):l),Z(r<10?"0".concat(r):r),Q(s<10?"0".concat(s):s))}),1e3);return function(){return clearInterval(t)}}}),[D,p]);return o.createElement("main",{className:"h-screen"},o.createElement("div",{className:"max-w-7xl mx-auto py-6 sm:px-6 lg:px-8"},o.createElement("div",{className:"max-w-2xl mx-auto px-5"},(N||x)&&o.createElement(u,null),null!=p&&p.submitted?o.createElement(o.Fragment,null,o.createElement("h2",{className:"text-5xl font-normal leading-normal mt-0 mb-2 text-purple-800"},null==p?void 0:p.quiz.title),o.createElement("h3",{className:"text-2xl font-semibold leading-normal mt-0 mb-2 text-gray-900"},"Result"),o.createElement("p",{className:"pl-5 font-semibold leading-normal mt-0 mb-2 text-gray-900"},"Score: ",null==p?void 0:p.score," / ",null==p?void 0:p.quiz.question.length),o.createElement("p",{className:"pl-5 font-semibold leading-normal mt-0 mb-2 text-gray-900"},"Date taken: ",(0,d.JU)(null==p?void 0:p.date_taken)," ",(0,d.Eg)(null==p?void 0:p.date_taken))):!N&&(null==p?void 0:p.quiz.title)&&o.createElement("form",{onSubmit:function(e){return function(e,a){e.preventDefault();var n=[];a.map((function(t){n.push({answerSelectedId:e.target["answer".concat(t.id)].value})})),v({answers:n,slug:t})}(e,null==p?void 0:p.quiz.question)}},o.createElement("div",{className:"flex"},o.createElement("div",{className:"w-24 mx-1 p-2 text-purple-800 rounded-lg"},o.createElement("div",{className:"font-mono text-4xl"},isNaN(b)?"00":b),o.createElement("div",{className:"pl-2 font-mono uppercase text-purple-800 text-sm leading-none"},"Days")),o.createElement("div",{className:"w-24 mx-1 p-2 text-purple-800 rounded-lg"},o.createElement("div",{className:"font-mono text-4xl"},isNaN(k)?"00":k),o.createElement("div",{className:"pl-2 font-mono uppercase text-purple-800 text-sm leading-none"},"Hours")),o.createElement("div",{className:"w-24 mx-1 p-2 text-purple-800 rounded-lg"},o.createElement("div",{className:"font-mono text-4xl"},isNaN(_)?"00":_),o.createElement("div",{className:"pl-2 font-mono uppercase text-purple-800 text-sm leading-none"},"Minutes")),o.createElement("div",{className:"w-24 mx-1 p-2 text-purple-800 rounded-lg"},o.createElement("div",{className:"font-mono text-4xl"},isNaN(D)?"00":D),o.createElement("div",{className:"pl-2 font-mono uppercase text-purple-800 text-sm leading-none"},"Seconds"))),o.createElement("h2",{className:"text-5xl font-normal leading-normal mt-0 mb-2 text-purple-800"},null==p?void 0:p.quiz.title),null==p?void 0:p.quiz.question.map((function(e,t){return o.createElement("div",{className:"mt-4",key:e.id},o.createElement("span",{className:"text-gray-700"},t+1,". ",e.title),o.createElement("section",{className:"mt-2 flex flex-col"},null==e?void 0:e.answer.map((function(t){return o.createElement("label",{className:"items-center",key:t.id},o.createElement("input",{type:"radio",className:"form-radio border-2 border-purple-500",name:"answer".concat(e.id),value:t.id}),o.createElement("span",{className:"ml-2"},t.answer_text))}))))})),o.createElement("button",{ref:I,className:"mt-6 text-purple-500 bg-transparent border border-solid border-purple-500\r hover:bg-purple-500 hover:text-white active:bg-purple-600 font-bold uppercase text-sm\r px-6 py-3 rounded-full outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150",type:"submit"},"Submit")))))}}}]);