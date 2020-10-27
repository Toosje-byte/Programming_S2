// main
package main

import (
	"html/template"
	"net/http"
)

type IndexPage struct {
	Title string
	Text1 string
	Text2 string
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	p := IndexPage{Title: "", Text1: "", Text2: ""}
	t, _ := template.ParseFiles("html_template.html")
	t.Execute(w, p)
}

func homeHandler(w http.ResponseWriter, r *http.Request) {
	p := IndexPage{Title: "Home", Text1: "Welcome to GoChat, the chatroom made with golang.", Text2: "You can chat on the chatroom page and you can find more information about GoChat on the about page."}
	t, _ := template.ParseFiles("html_template.html")
	t.Execute(w, p)
}

func chatroomHandler(w http.ResponseWriter, r *http.Request) {
	p := IndexPage{Title: "Chatroom", Text1: "UNDER CONSTRUCTION", Text2: ""}
	t, _ := template.ParseFiles("html_template.html")
	t.Execute(w, p)
}

func aboutHandler(w http.ResponseWriter, r *http.Request) {
	p := IndexPage{Title: "About", Text1: "This website was created for a school exercise.", Text2: ""}
	t, _ := template.ParseFiles("html_template.html")
	t.Execute(w, p)
}

func main() {
	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/Home", homeHandler)
	http.HandleFunc("/Chatroom", chatroomHandler)
	http.HandleFunc("/About", aboutHandler)
	http.ListenAndServe(":8080", nil)
}
