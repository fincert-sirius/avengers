(() => {
	const dark_theme = "/static/css/dark-theme.css";
	const light_theme = "/static/css/light-theme.css";

	const set_theme = (theme) => {
		$(".theme").remove();
		$("#sova-box").empty();

		$("head").append(
			`<link rel="stylesheet" href="${theme}" class="theme">`
		);

		if (theme == light_theme) {
			$("#sova-box").append(
				`<img src="/static/img/sova.png" class="top-img-wigth change-theme">`
			);
		}
		else {
			$("#sova-box").append(
				`<img src="/static/img/sova_white.png" class="top-img-wigth change-theme">`
			);
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