(() => {
	const dark_theme = "/static/css/dark-theme.css";
	const light_theme = "/static/css/light-theme.css";

	const set_theme = (theme) => {
		$(".theme").remove();
		$("#sova-box").empty();
		$("footer").empty();

		$("head").append(
			`<link rel="stylesheet" href="${theme}" class="theme">`
		);

		if (theme == light_theme) {
			$("#sova-box").append(
				`<img src="/static/img/sova.png" class="top-img-wigth change-theme">`
			);
			$("footer").append(`
				<div class="uk-section uk-section-muted uk-section-xsmall uk-padding-small">
					<div class="uk-container uk-flex uk-flex-between uk-flex-bottom">
						<div class="uk-flex uk-flex-column">
					        <a href="/about" class="uk-link-muted">О нас</a>
					        <div class="uk-inline">
						        <span uk-icon="icon: github"></span>
						        <a href="https://github.com/fincert-sirius/avengers" class="uk-link-muted">GitHub</a>
					        </div>
						</div>
						<div>
							<p>&#169; Copyleft Sirius EC 2019</p>
						</div>
					</div>
				</div>
			`);
		}
		else {
			$("#sova-box").append(
				`<img src="/static/img/sova_white.png" class="top-img-wigth change-theme">`
			);
			$("footer").append(`
				<div class="uk-section uk-section-secondary uk-section-xsmall uk-padding-small">
					<div class="uk-container uk-flex uk-flex-between uk-flex-bottom">
						<div class="uk-flex uk-flex-column">
					        <a href="/about" class="uk-link-muted">О нас</a>
					        <div class="uk-inline">
						        <span uk-icon="icon: github-alt"></span>
						        <a href="https://github.com/fincert-sirius/avengers" class="uk-link-muted">GitHub</a>
					        </div>
						</div>
						<div>
							<p>&#169; Copyleft Sirius EC 2019</p>
						</div>
					</div>
				</div>
			`);
		}
	};

	const next_theme = (theme) => {
		if (theme == light_theme)
			return dark_theme;
		return light_theme;
	};

	const get_curr_theme = () => {
		return localStorage.getItem("theme") || light_theme;
	};

	const set_curr_theme = (theme) => {
		localStorage.setItem("theme", theme)
	}

	const change_theme = () => {
		let t = get_curr_theme();
		t = next_theme(t);
		set_curr_theme(t);
		set_theme(t);
	};

	$("#sova-box").on('click','.change-theme', change_theme);
	set_theme(get_curr_theme());
})();