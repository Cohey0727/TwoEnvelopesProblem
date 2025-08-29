.PHONY: render render-intro clean

render-intro:
	uv run manim src/01_introduction/introduction.py TwoEnvelopesIntro -pql

render: clean render-intro

clean:
	rm -rf media/*

help:
	@echo "Available commands:"
	@echo "  render-intro  - Render introduction video"
	@echo "  render        - Render all videos"
	@echo "  clean         - Clean generated media files"
	@echo "  help          - Show this help message"