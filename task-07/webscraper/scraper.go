package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"

	"github.com/gocolly/colly"
)

func main() {

	fName := "data.csv"
	file, err := os.Create(fName)
	if err != nil {
		log.Fatalf("Could not create file, err: %q", err)
		return
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	c := colly.NewCollector(
		colly.AllowedDomains("forbes.com", "www.forbes.com"),
	)

	c.OnHTML(".scrolly-table", func(e *colly.HTMLElement) {
		links := e.ChildAttrs("ng-href", "a")
		fmt.Println(links)
	})
	c.Visit("https://www.forbes.com/real-time-billionaires/#24b3862a3d78")
}
